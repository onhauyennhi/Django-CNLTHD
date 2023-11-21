from django.contrib import admin
from auth_app.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username', 'first_name', 'last_name') 
    readonly_fields = ('last_login', 'date_joined')    
    ordering = ('-date_joined',)  

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)
