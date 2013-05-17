from django.core.management.base import BaseCommand

from registrations.models import Participant
from registrations.tasks import send_confirmation_email


class Command(BaseCommand):
    args = '<participant_id>'
    help = 'Send mails'
    
    def handle(self, *args, **options):
        for participant_id in args:
            send_confirmation_email(participant_id)
        if not args:
            participants = Participant.objects.filter(confirmed=False)
            for participant in participants:
                send_confirmation_email(participant.id)
