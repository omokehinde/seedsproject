from django.http import HttpResponse
from django.shortcuts import render
from .models import NameNEmail

def index(request):
	all_info = NameNEmail.objects.all()
	context = {
		'all_info': all_info
	}
	return render(request, 'info/index.html', context)
