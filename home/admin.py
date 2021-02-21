from django.contrib import admin

# Register your models here.

from .models import Contact,ContactInformation

admin.site.register(Contact)

admin.site.register(ContactInformation)

