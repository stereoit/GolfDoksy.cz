from django.contrib import admin
from tournaments.models import Tournament


class TournamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name','starts_on')
    filter_horizontal = ('players',)

admin.site.register(Tournament,TournamentAdmin)
