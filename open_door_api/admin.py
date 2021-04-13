from django.contrib import admin

from open_door_api import models

# Dando acceso al administrador para modificar el modelo UserProfile
admin.site.register(models.UserProfile)
admin.site.register(models.Door)

