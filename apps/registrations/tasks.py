import logging
from celery.decorators import task

from django.core.mail import send_mail
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string

from .models import Participant

logger = logging.getLogger('douhack.{0}'.format(__name__))

@task
def send_confirmation_email(participant_id):
    """
    Send confirmation email to participant
    """
    try:
        participant = Participant.objects.get(id=participant_id)
    except Participant.DoesNotExist:
        logger.error("Such participant doesn't exist") 
    else:
        data = {
            'participant': participant
        }
        params = {
            'subject': _('Mail subject'),
            'message': render_to_string('registrations/message.txt', data),
            'from_email': 'douhacksevastopol@gmail.com',
            'recipient_list': [participant.email]
        }
        send_mail(**params)
