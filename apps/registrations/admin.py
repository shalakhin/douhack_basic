from django.contrib import admin

from .models import Participant


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'city', 'created', 'updated', 'confirmed']
    list_filter = ('city', 'created', 'updated', 'confirmed',)
    readonly_fields = ('confirmation_code', 'created', 'updated',)


admin.site.register(Participant, ParticipantAdmin)
