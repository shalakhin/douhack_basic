from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _

from registrations.forms import ParticipantForm


def home(request):
    """
    Home page
    """
    context = {}
    return render(request, 'home.html', context)


def contacts(request):
    """
    Contact page
    """
    context = {}
    return render(request, 'contacts.html', context)


def register(request):
    """
    Register page with
    """
    form = ParticipantForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.INFO, _('You are registered'))
            return redirect('home')
    context = {
        'form': form        
    }
    return render(request, 'registrations/form.html', context)
