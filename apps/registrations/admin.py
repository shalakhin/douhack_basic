from django.contrib import admin

from .models import Participant


class ParticipantAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'contacts','email', 'city', 'need_apartments', 'confirmed'
        'need_railway_station','created', 'updated', 'internal_comments']
    list_filter = ('city', 'created', 'updated', 'confirmed',
        'need_apartments', 'need_railway_station')
    readonly_fields = ('confirmation_code', 'created', 'updated',)


admin.site.register(Participant, ParticipantAdmin)
