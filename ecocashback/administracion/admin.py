from django.contrib import admin
from .models import (Comuna, Evento, Region)
# Register your models here.
admin.site.register(Comuna)
admin.site.register(Evento)
admin.site.register(Region)