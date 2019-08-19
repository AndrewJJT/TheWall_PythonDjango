from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    if request.method == 'GET':
        return render(request, "user_info/index.html")
    # if request.method == 'POST':
    #     errors = User.objects.basic_validator(request.POST)
    #     if len(errors) > 0:
    #         for key,value in errors.items():
    #             messages.error(request, value)
    #     else:
    #         User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password = request.POST['password'])
    #         return render(request, "main_app/checkout.html")
def sucessfullogin(request, id):
    if "login" in request.session:
        user = User.objects.get(id = id)
        userfullname = user.first_name + ", " + user.last_name
        content = {
            "username": userfullname,
        }
        return render(request, "user_info/loggedinpage.html", content)
    else: 
        return redirect('/')
    

def register(request):
    if request.method == 'POST':
        registrationerrors = User.objects.basic_validator(request.POST)
        if len(registrationerrors) > 0:
            for key,value in registrationerrors.items():
                messages.error(request, value, extra_tags="register")
            return redirect('/')
        else:
            request.session['login'] = True
            hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password = hashedpw)
            user = list(User.objects.filter(email = request.POST['email']))
            return redirect('/sucessfullogin/' + str(user[0].id))

def login(request):
    user = list(User.objects.filter(email = request.POST['email']))
    # user = User.objects.get(email = request.POST['email'])
    print(user)
    if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
        request.session['login'] = True
        # content_app = 'content_info'
        # return redirect('/sucessfullogin/'+ str(user[0].id))
        return redirect('/content/'+ str(user[0].id))
    else:
        login_errors = User.objects.validator_for_login()
        for key,value in login_errors.items():
            messages.error(request,value, extra_tags="login")
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')