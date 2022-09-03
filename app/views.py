from unicodedata import name
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def user (request,name):
    return render(request,'user.html',{'user':name})

def user1(request):
    name=request.POST['user']
    return redirect('user/'+name)