from django.shortcuts import render,HttpResponse
from .models import Link
from .forms import SubscriberForm

# Create your views here.
def home(request):
    template = 'home.html'
    obj = Link.objects.all()
    form = SubscriberForm()
    if obj is not None:
        o = {'objects':obj,'form':form}
    else:
        o = {'objects':None,'form':form}
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request,template,o)
    # return HttpResponse("Home here")