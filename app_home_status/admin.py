from django.contrib import admin

# Register your models here.
from .models import Status, Comments

admin.site.register(Status)
admin.site.register(Comments)