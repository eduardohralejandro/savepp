from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class ExtendedUser(AbstractUser):
    avatar = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True) maybe change it for default value


class Bill(models.Model):
    id = models.AutoField(primary_key=True, db_column='bill_id', unique=True)
    title = models.TextField(null=False, blank=False)
    amount = models.IntegerField()
    note = models.TextField(null=True, blank=True)
    document = models.TextField(null=True, blank=True)
    settled = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    bill_created_by_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Transaction(models.Model):
    id = models.AutoField(
        primary_key=True, db_column='transaction_id', unique=True)
    amount = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    settled_transaction = models.BooleanField(default=False)
    bill_owned_by_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bill_owned_by_user_id'
    )
    bill_created_by_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bill_created_by_user_id'
    )
    bill_id_on_transaction = models.OneToOneField(
        Bill,
        on_delete=models.CASCADE,
        related_name='bill_id_on_transaction'
    )


class Category(models.Model):
    id = models.AutoField(
        primary_key=True, db_column='category_id', unique=True)
    title = models.TextField(null=False, blank=False)
    bill_id_on_category = models.OneToOneField(
        Bill,
        on_delete=models.CASCADE,
        related_name='bill_id_on_category'
    )
