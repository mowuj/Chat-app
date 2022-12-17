from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
    user=request.user.profile
    friends=user.friends.all()
    context={'user':user,'friends':friends}
    return render(request,'index.html',context)

def detail(request,pk):
    friend=Friend.objects.get(profile_id=pk)
    user =request.user.profile
    profile=Profile.objects.get(id=friend.profile.id)
    chats=ChatMessage.objects.all()
    rcv_chats=ChatMessage.objects.filter(msg_sender=profile,msg_receiver=user,seen=False)
    rcv_chats.update(seen=True)
    form=ChatMessageForm()
    if request.method=="POST":
        form=ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message=form.save(commit=False)
            chat_message.msg_sender=user
            chat_message.msg_receiver=profile
            chat_message.save()
            return redirect('detail',pk=friend.profile.id)
    context={'friend':friend,'form':form,'user':user,'profile':profile,'chats':chats,"num":rcv_chats.count()}
    return render(request,'detail.html',context)

def sentMessages(request,pk):
    user=request.user.profile
    friend=Friend.objects.get(profile_id=pk)
    profile=Profile.objects.get(id=friend.profile.id)
    data=json.loads(request.body)
    new_chat=data['msg']
    new_chat_message=ChatMessage.objects.create(body=new_chat,msg_sender=user,msg_receiver=profile,seen=False)
    return JsonResponse(new_chat_message.body,safe=False)

def receivedMessages(request,pk):
    user=request.user.profile
    friend=Friend.objects.get(profile_id=pk)
    profile=Profile.objects.get(id=friend.profile.id)
    chat_array=[]
    chats=ChatMessage.objects.filter(msg_sender=profile,msg_receiver=user)
    for chat in chats:
        chat_array.append(chat.body)
    return JsonResponse(chat_array,safe=False)

# def getNotification(request):
#     user=request.user.profile
#     friends=user.friends.all()
#     notify=[]
#     for friend in friends:
#         chats=ChatMessage.object.filter(msg_sender__id=friend.profile.id,msg_receiver=user,seen=False)
#         notify.append(chats.count())
#     return JsonResponse(notify,safe=False)

def chatNotification(request):
    user = request.user.profile
    friends = user.friends.all()
    arr = []
    for friend in friends:
        chats = ChatMessage.objects.filter(msg_sender__id=friend.profile.id, msg_receiver=user, seen=False)
        arr.append(chats.count())
    return JsonResponse(arr, safe=False)