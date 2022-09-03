from django.shortcuts import render,redirect
from .models import task

# Create your views here.
def index(request):
    return render(request,'index.html')

def user (request,name):
    list=task.objects.filter(Name=name,review=False).values()
    return render(request,'user.html',{'user':name,'list':list,'i':0,'len':list.count})

def user1(request):
    name=request.POST['user']
    return redirect('user/'+name)

def update(request):
    name=request.POST['name']
    id=request.POST['id']
    temp=task.objects.get(id=id)
    temp.review=True
    temp.save()
    return redirect('/user/'+name)