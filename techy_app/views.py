from django.shortcuts import render, redirect
from .forms import ContactForm, PotentialCustomerForm
from .models import Contact, PotentialCustomer


def home_view(request):
    print("Rendering home.html")
    return render(request, 'index.html') 

def about_view(request):
    print("Rendering about.html")
    return render(request, 'about.html') 

def service_view(request):
    print("Rendering service.html")
    return render(request, 'service.html') 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success') 
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'success.html')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def potential_customer(request):
    if request.method == 'POST':
        form = PotentialCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_success')
    else:
        form = PotentialCustomerForm()
    return render(request, 'potential_customer.html', {'form': form})


def customer_success(request):
    return render(request, 'customer_success.html')



def potential_customer_list(request):
    customers = PotentialCustomer.objects.all()
    return render(request, 'potential_customer_list.html', {'customers': customers})
