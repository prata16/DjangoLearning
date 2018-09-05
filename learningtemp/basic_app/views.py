from django.shortcuts import render

# Create your views here.
def index(request):
	my_dict={'text': 'hello world', 'name':'pratap','number':100}
	return render(request, 'basic_app/index.html', my_dict)

def other(request):
	return render(request, 'basic_app/other.html')

def relative(request):
	return render(request, 'basic_app/relative_url_tem.html')

