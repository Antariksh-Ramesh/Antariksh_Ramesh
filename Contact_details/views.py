from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'Contact_details/contact_list.html', {'contacts': contacts})

def contact_create(request):
    form = ContactForm(request.POST) if request.method == 'POST' else ContactForm()
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'Contact_details/contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST, instance=contact) if request.method == 'POST' else ContactForm(instance=contact)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, 'Contact_details/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list')

