from django.contrib import admin
from myapp.models import Musician, Album, User, Student

# Register your models here.
@admin.register(Musician)
class MusicianAdimin(admin.ModelAdmin):
	list_display = ["first_name", "last_name","instrument"]
	search_fields = ['first_name']
	list_filter = ['instrument']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	list_display=['artist','name','release_date','num_stars']
	search_fields=['name']
	list_filter=['release_date','num_stars']
	ordering=['-release_date'] #descending order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ["first_name", "last_name","email"]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display=['name','email', 'birth_date','password']

