from django.contrib import admin
from basicapp.models import UserProfileInfo

# Register your models here.
@admin.register(UserProfileInfo)
class UserInfoAdmin(admin.ModelAdmin):
	pass