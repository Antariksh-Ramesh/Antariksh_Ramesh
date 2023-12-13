from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

from django.urls import get_resolver


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'Contact_details/contact_list.html', {'contacts': contacts})

def contact_create(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'Contact_details/contact_create.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'Contact_details/contact_update.html', {'form': form, 'contact': contact})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'Contact_details/contact_delete.html', {'contact': contact})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'Contact_details/contact_detail.html', {'contact': contact})