from django.http import HttpResponse
from django.tempate import loader

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())