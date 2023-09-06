from rest_framework.serializers import ModelSerializer
from .models import Bill, Transaction, ExtendedUser, Category


class BillSerializer(ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class ExtendedUserSerialiazer(ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'