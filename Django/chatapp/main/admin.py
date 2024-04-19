from django.contrib import admin

# Register your models here.
from .models import User, Talk

admin.site.register(User)
admin.site.register(Talk)