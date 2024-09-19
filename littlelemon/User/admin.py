from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from restaurant.models import Menu


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','menu_item_description' ,'uploaded_by', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('uploaded_by',)




admin.site.register(Menu,MenuAdmin)