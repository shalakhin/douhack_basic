import datetime

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from registrations.forms import ParticipantForm
from registrations.models import Participant


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
        messages.add_message(
            request, messages.INFO, _('Sorry but registration is closed!'))
        return redirect('home')
        # if form.is_valid():
        #     form.save()
        #     messages.add_message(
        #         request, messages.INFO, _('You are registered'))
        #     return redirect('home')
    context = {
        'form': form        
    }
    return render(request, 'registrations/form.html', context)


def confirm_registration(request, id, code):
    """
    Confirm participation
    """
    participant = get_object_or_404(Participant, id=id)
    if participant.confirmation_code == code:
        participant.confirmed = True
        participant.updated = datetime.datetime.now()
        participant.save()
        messages.add_message(
            request,
            messages.INFO,
            _('You successfully confirmed participation! Thanks!')
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            _("You haven't confirmed your participation!")
        )
    return redirect(reverse('home'))
