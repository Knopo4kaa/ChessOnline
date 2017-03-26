from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.context_processors import csrf
from django.template.loader import render_to_string
import datetime
from .models import User

# Create your views here.
def registration(request):
    c = {}
    validation = {}
    validation.update(csrf(request))
    c = RequestContext(request, validation)
    if request.user.is_authenticated():
        c['user'] = True
        if request.user.is_superuser:
            c['admin']=True
    return HttpResponse(render_to_string('registration.html',c))

def createuser(request):
    c = {}
    validation={}
    validation.update(csrf(request))
    c = RequestContext(request, validation)
    if request.method == 'POST':


        username = request.POST['display_name']
        password = request.POST['password']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        conf_pass=request.POST['password_confirmation']
        email=request.POST['email']
        try:
            user = User.objects.get(username=username)
            if user is not None:
                c['main_error'] = True
                c['Error']='This user already exists'
                return HttpResponse(render_to_string('registration.html', c))
        except BaseException:
            if conf_pass != password:
                c['main_error'] = True
                c['Error'] = 'Passwords are different'
                return HttpResponse(render_to_string('registration.html', c))
            c.update(csrf(request))
            new_user = User.objects.create_user(username=username,email = email, password=password, first_name=first_name, last_name=last_name)
            new_user.save



            return redirect('/registration')
    return redirect('/registration')

def login_page(request):
    c = {}
    validation = {}
    validation.update(csrf(request))
    c = RequestContext(request, validation)
    if request.user.is_authenticated():
        c['user'] = True
    return HttpResponse(render_to_string('login.html', c))



def log(request):
    c={}
    validation = {}
    validation.update(csrf(request))
    c = RequestContext(request, validation)
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        try:
            user_model=User.objects.get(username=username)
            if not user_model.is_active:
                c['main_error'] = True
                c['Error'] = 'This user is not active'
                return HttpResponse(render_to_string('registration.html', c))
            user = authenticate(username=username, password=password)
            c['main_error']=False
            if user is not None:
                login(request, user)
                return redirect('/')
        except BaseException:
            c['main_error'] = True
            c['Error'] = 'This user is not exist'
            return HttpResponse(render_to_string('registration.html', c))






