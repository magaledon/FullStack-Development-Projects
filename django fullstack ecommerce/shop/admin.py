from django.contrib import admin
from .models import *

# Register your models here.

"""class ctadmin(admin.ModelAdmin):
    list_display=('name','image','description')
admin.site.register(Category,ctadmin)
"""

admin.site.register(Category)
admin.site.register(Products)
