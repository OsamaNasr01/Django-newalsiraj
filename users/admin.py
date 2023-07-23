from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('first_name','last_name', 'phone_number',)}


admin.site.register(User, UserAdmin)