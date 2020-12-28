from django.shortcuts import render,HttpResponse
from .models import Link

# Create your views here.
def home(request):
    template = 'home.html'
    obj = Link.objects.all()
    if obj is not None:
        o = {'objects':obj}
    else:
        o = {'objects':None}
    return render(request,template,o)
    # return HttpResponse("Home here")