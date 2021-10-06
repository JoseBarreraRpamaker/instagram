from django.contrib import admin

from users.models import Profile

from django.contrib import admin

# Register your models herec

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display= ('pk','user','phone_number','website','pcture')
    list_display_links=('pk','user')
    list_editable=('website','pcture','phone_number')