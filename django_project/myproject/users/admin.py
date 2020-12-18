from django.contrib import admin
from .models import Adduser
# Register your models here.

# admin.site.register(Adduser)
@admin.register(Adduser)
class UserModel(admin.ModelAdmin):
    list_display = ['fname', 'lname']
    search_fields = ['fname']
