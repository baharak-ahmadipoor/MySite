from django.contrib import admin

from .models import contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date')
    search_fields= ('name',)
    list = ('created_date',)


admin.site.register(contact, ContactAdmin)