from django.contrib import admin
from django.urls import path
from techy_app.views import home_view, about_view, contact, contact_success, contact_list, potential_customer, customer_success, potential_customer_list, service_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about', about_view, name='about'),
    path('contact', contact, name='contact'),
    path('service', service_view, name='service'),
    path('contact_success/', contact_success, name='contact_success'),
    path('contact_list/', contact_list, name='contact_list'),
    path('potential-customer/', potential_customer, name='potential_customer'),
    path('potential-customer-list/', potential_customer_list, name='potential-customer-list'),
    path('customer-success/', customer_success, name='customer_success')

]
