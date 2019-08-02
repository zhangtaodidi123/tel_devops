from django.contrib import admin

# Register your models here.
from django.db import models

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(User,UserAdmin)