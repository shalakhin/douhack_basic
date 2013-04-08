from django import forms

from .models import Participant


class ParticipantForm(forms.ModelForm):
    """
    Form to be used for users registration
    """

    class Meta:
        model = Participant
        fields = ('name', 'email', 'technologies', 'city',)
