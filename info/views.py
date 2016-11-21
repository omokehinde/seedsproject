from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import NameNEmail
from django.core.urlresolvers import reverse
from info.forms import EmailNameForm

def index(request):
	return render(request, 'info/index.html')

def list(request):
	all_info = NameNEmail.objects.all()
	context = {
		'all_info': all_info
	}
	return render(request, 'info/list.html', context)

def add(request):
	
	if request.method == 'POST':
		form = EmailNameForm(request.POST)
		if form.is_valid:
			
			info = form.save(commit=False)

			#clean (normalized) data
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			info.save()

			return HttpResponseRedirect('/list')
	else:
			form = EmailNameForm() # This returns the user to the form 
		#return render(request, 'info/list.html')
	return render(request, 'info/add.html', {'form': form})


	