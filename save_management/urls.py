from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("admin/", admin.site.urls),

    path('all-bills', views.get_bills, name='bills'),
]
