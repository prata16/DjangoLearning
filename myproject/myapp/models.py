from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
    	return self.first_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField() 

class Student(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    birth_date = models.DateField()
    password = models.CharField(max_length=10,default='DEFAULT VALUE')
