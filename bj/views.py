from django.shortcuts import render



# Create your views here.

def home(request):
	return render(request, 'bj/home.html', {})
def login(request):
	return render(request, 'bj/login.html', {})
def registr(request):
	return render(request, 'bj/registr.html', {})
def contacts(request):
	return render(request, 'bj/contacts.html', {})
def bj(request):
	return render(request, 'bj/bj.html', {})
def rasp(request):
	return render(request, 'bj/rasp.html', {})




