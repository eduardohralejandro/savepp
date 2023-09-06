from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Bill, ExtendedUser, Transaction, Category
from .serializers import BillSerializer, TransactionSerializer, ExtendedUserSerialiazer, CategorySerializer


@api_view(['GET'])
def get_bills(request):
    current_user_id = request.user.id

    try:
        user = ExtendedUser.objects.filter(id=current_user_id)
        user_payed_by = ExtendedUser.objects.all()

        transactions = Transaction.objects.filter(
            bill_owned_by_user_id_id=current_user_id)
        transaction_serialized = TransactionSerializer(transactions, many=True)

        bills = Bill.objects.all()
        bill_serialized = BillSerializer(bills, many=True)

    except user.DoesNotExist:
        return HttpResponse("The requested Model does not exist.", status=404)
    except transactions.DoesNotExist:
        return HttpResponse("The requested Model does not exist.", status=404)
    except bills.DoesNotExist:
        return HttpResponse("The requested Model does not exist.", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

    common_bills = []

    for bills in bill_serialized.data:
        for transactions in transaction_serialized.data:
            if bills['id'] == transactions['bill_id_on_transaction']:

                user_creator = user_payed_by.filter(
                    id=bills['bill_created_by_user_id'])
                serialized_user = ExtendedUserSerialiazer(
                    user_creator, many=True)

                category = Category.objects.all().filter(
                    bill_id_on_category=bills['id'])
                serialized_category = CategorySerializer(category, many=True)

                bills['username'] = serialized_user.data[0].get('username')
                if serialized_category.data:
                    bills['category'] = serialized_category.data[0].get(
                        'title')
                common_bills.append(bills)
                break

    current_user_transaction = {
        "name": str(user[0]),
        "transactions": transaction_serialized.data,
        "bills": common_bills
    }

    return Response(current_user_transaction)
