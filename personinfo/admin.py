from django.contrib import admin

# Register your models here.
from .models import PersonApp
from .models import Department

admin.site.register(PersonApp)
admin.site.register(Department)

