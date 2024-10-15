# contact/admin.py
from django.contrib import admin
from .models import Contact, PotentialCustomer

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

@admin.register(PotentialCustomer)
class PotentialCustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'message')
