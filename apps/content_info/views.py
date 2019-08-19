from django.shortcuts import render, redirect
from .models import Comment, Message
from ..user_info.models import User
import datetime
from django.utils import timezone
import pytz

# Create your views here.

def index(request,id):
    current_tz = pytz.timezone("US/Pacific")
    timezone.activate(current_tz)
    if 'login' in request.session:
        selecteduser = User.objects.get(id=id)
        messages = Message.objects.all().order_by("-created_at")
        comments = Comment.objects.all().order_by("-created_at")

        print("time directly out of database: ", selecteduser.created_at) #at UTC time
        rightnow = datetime.datetime.now(tz=pytz.UTC) # change now() to UTC time
        print("time now: ", rightnow)
        timedif = rightnow - selecteduser.created_at # now with same timezone, can subtract to get duration
        print("time difference: ", timedif)

        content ={
            "id": selecteduser.id,
            "fname":selecteduser.first_name,
            "lname":selecteduser.last_name,
            "messages": messages,
            "comments": comments,
        }
        return render(request, 'content_info/index.html', content)
    else:
        return redirect("/")

def addpost(request,id):
    Message.objects.create(message = request.POST['message'], user=User.objects.get(id=id))
    return redirect("/content/" + id)

def addcomment(request,id):
    Comment.objects.create(comment = request.POST['comment'], user=User.objects.get(id=id), message=Message.objects.get(id=request.POST['messageid']))
    return redirect("/content/" + id)

def deletemessage(request,id,mid):
    messagetoremove = Message.objects.get(id=mid)
    modifieddate = make_naive(messagetoremove.created_at) # local system time zone
    print("time directly out of database: ", messagetoremove.created_at)
    print("modified time in database: ", modifieddate)
    rightnow = datetime.datetime.now() #local system time zone
    print("time now: ", rightnow)
    timedif = rightnow - modifieddate
    print("time difference: ", timedif)
    messagetoremove.delete()
    return redirect("/content/" + id)