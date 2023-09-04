from rest_framework.serializers import ModelSerializer
from .models import Bill


class BillSerializer(ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'