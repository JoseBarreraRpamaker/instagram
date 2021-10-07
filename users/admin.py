from django.contrib import admin
from posts.models import Users
import users

from users.models import Profile

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User

# Register your models herec

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display= ('pk','user','phone_number','website','pcture')
    list_display_links=('pk','user')
    list_editable=('website','pcture','phone_number')
    search_fields=('user__email','user__username')
    list_filter=('created','user__is_active')
    fieldsets=(
          ('profile'),{
          'fields' : ('user','picture'),
           
          }),

class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete =  False
    verbose_name_plural =  'profiles' 


class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)
     
    


admin.site.unregister(User)
admin.site.register(User,UserAdmin)


