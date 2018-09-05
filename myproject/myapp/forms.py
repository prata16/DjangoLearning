from django import forms
from django.core import validators
from myapp.models import Student

def check_for_z(value):
	if value[0].lower() != 'z':
		raise forms.ValidationError("Name must start with \'z\' letter")

class NameForm(forms.Form):
	name = forms.CharField()
	email= forms.EmailField()
	verify_email = forms.EmailField(label="enter email once again")
	text = forms.CharField(widget=forms.Textarea) 
	bootcatcher = forms.CharField(required= False,
								  widget=forms.HiddenInput,
								  validators=[validators.MaxLengthValidator(0)])

	def clean(self):
		all_clean_data= super().clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']

		if email != vmail:
			raise forms.ValidationError("Make sure email match")

	"""
	form validators
	def clean_botcatcher(self):
		botcatcher= self.cleaned_data['botcatcher']
		if len(botcatcher) > 0:
			raise forms.ValidationError("GOTCHA BOT!")
		return botcatcher
	""" 
class StudentForm(forms.ModelForm):
	birth_date = forms.DateField(widget=forms.DateInput)
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Student
		fields = "__all__"