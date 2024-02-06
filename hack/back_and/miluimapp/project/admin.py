from django.contrib import admin
from .models import Miluimnick


class AdminMiluimnick(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "name_business", "business_city", "business_street", "business_address", "business_type", "link_google_maps")

admin.site.register(Miluimnick, AdminMiluimnick)
