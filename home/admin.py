from django.contrib import admin
from .models import Client
from .models import Subscribe


# Register your models here.

admin.site.register(Client)
admin.site.register(Subscribe)