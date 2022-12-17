from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    user=request.user.profile
    friends=user.friends.all()
    context={'user':user,'friends':friends}
    return render(request,'index.html',context)

def detail(request,pk):
    friend=Friend.objects.get(profile_id=pk)
    context={'friend':friend}
    return render(request,'detail.html',context)