from django.contrib import admin

# Register your models here.

from .models import Contact,ContactInformation,Testonomial

admin.site.register(Contact)

admin.site.register(ContactInformation)

admin.site.register(Testonomial)

