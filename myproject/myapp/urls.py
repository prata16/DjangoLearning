from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('form/', views.name_form, name='form'),
    path('student/', views.student_form, name='student')
    
]