from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    """ Contact Us Page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contact Form sucessfully submitted.')
            return redirect('home')
        else:
            messages.error(request, 'Failed to submit contact form. Please ensure the form is valid.')    
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
