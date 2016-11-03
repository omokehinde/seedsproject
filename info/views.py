from django.http import HttpResponse
from django.template import loader
from .models import NameNEmail

def index(request):
	all_info = NameNEmail.objects.all()
	template = loader.get_template('info/index.html')
	context = {
		'all_info': all_info
	}
	return HttpResponse(template.render(context, request))
