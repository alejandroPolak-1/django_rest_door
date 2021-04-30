from django.contrib import admin

# Register your models here.
from .models import Personal, Door, PersonalByDoors

admin.site.register(Personal)
admin.site.register(Door)
admin.site.register(PersonalByDoors)