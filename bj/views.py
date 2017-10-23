from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'bj/home.html', {})
def login(request):
	return render(request, 'bj/login.html', {})
def registr(request):
	return render(request, 'bj/registr.html', {})