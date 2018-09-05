from django.shortcuts import render,HttpResponse
from myapp.models import Musician, Album, User, Student
from . import forms

# Create your views here.
def home(request):
	my_dict = {'inser_me':"this is inserted from views"}
	return render(request, 'home.html', my_dict)
	#return HttpResponse("<h1>HOME page</h1>")

def about(request):
	album_list = Album.objects.order_by('release_date')
	date_dict ={'album_records': album_list}
	return render(request,'index.html', date_dict)
	#return HttpResponse("<h2>about page</h2>")

def myusers(request):
	user_list = User.objects.order_by("first_name")
	name = {'name_details':user_list}
	return render(request, 'user.html', name)
	#return HttpResponse("<h1> User list page</h1>")

def name_form(request):
	form = forms.NameForm()

	if request.method == "POST":
		form = forms.NameForm(request.POST)

		if form.is_valid():
			print("VALIDATION SUCCESS!")
			print("Name: "+form.cleaned_data['name'])
			print("Email: "+form.cleaned_data['email'])
			print("Text: "+form.cleaned_data['text'])

	return render(request, 'forms_page.html', {'form':form })

def student_form(request):
	form = forms.StudentForm()
	if request.method == "POST":
		form = forms.StudentForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return home(request)
		else:
			print("ERROR 404")

	return render(request, 'studentform.html', {'form':form })