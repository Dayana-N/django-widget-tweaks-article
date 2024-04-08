from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)
