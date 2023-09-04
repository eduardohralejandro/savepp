
from .models import Bill
from .serializers import BillSerializer

from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


# First tested view get all bills.
@api_view(['GET'])
def get_bills(request):
    notes = Bill.objects.all().order_by('-created')
    serializer = BillSerializer(notes, many=True)
    return Response(serializer.data)