from django.contrib import admin

from .models import Participant


class ParticipantAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'contacts','email', 'city',
        'need_apartments', 'confirmed', 'need_railway_station',
        'internal_comments_shortly']
    list_filter = ('city', 'created', 'updated', 'confirmed',
        'need_apartments', 'need_railway_station')
    readonly_fields = ('confirmation_code', 'created', 'updated',)

    def internal_comments_shortly(self, obj):
        """
        Show first 100 characters of the comment
        """
        return obj.internal_comments[0:99]

    internal_comments_shortly.short_description = 'Internal comments'

admin.site.register(Participant, ParticipantAdmin)
