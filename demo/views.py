from django.http import HttpResponse


def index(request):
	return HttpResponse('I am a programmer')

def login(request):
	return HttpResponse('You are logged in')

def logout(request):
	return HttpResponse('You are logged out')


