from django.contrib import admin

# Register your models here.

from .models import Industry,Job,Person

admin.site.register(Industry)
admin.site.register(Job)
admin.site.register(Person)
