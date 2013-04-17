import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Participant(models.Model):
    """
    Those who filled registration form
    """
    name = models.CharField(_('Name'), max_length=255)
    contacts = models.CharField(_('Your phone number'), max_length=255)
    email = models.EmailField(_('E-mail'), max_length=255, unique=True)
    city = models.CharField(_('City'), max_length=255, blank=True)
    need_apartments = models.BooleanField(
        _('Need help apartments'), blank=True)
    need_railway_station = models.BooleanField(
        _('Need help to find railway station'), blank=True)
    how_got_info = models.TextField(
        _('How did you get to know about the event?'), blank=True)

    confirmation_code = models.CharField(_('Confirmation code'),
        editable=False, max_length=255, blank=True)
    confirmed = models.BooleanField(_('Participation confirmed'),
            default=False, blank=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True, blank=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True, blank=True)
    internal_comments = models.TextField(_('Internal comments'),
        help_text=_('visible only for registered users'), blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # we have to generate confirmation code
        if not self.confirmation_code:
            self.confirmation_code = uuid.uuid4().__str__()
        super(Participant, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-updated', '-created']
