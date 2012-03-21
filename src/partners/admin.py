from django.contrib import admin
from partners.models import Partner

admin.site.register(Partner)

class PartnerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
