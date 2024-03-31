from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms
from . import translator
from . import models
from random import choice
import string

# Create your views here.
def generate_id():
    characters = string.ascii_letters + string.digits
    id = ""
    return ''.join([choice(characters) for i in range(10)])
    for x in range(22):
        id+=choice(characters)
    return id

def generate_password():
    characters = string.ascii_letters + string.punctuation + string.digits
    password = ""
    for x in range(6):
        password+=choice(characters)
    return password

def index_view(request):
    answer = ''
    TextInputForm = forms.TextInputForm()
    if request.method == 'POST':
        TextInputForm = forms.TextInputForm(request.POST)
        if  TextInputForm.is_valid():
            userInput = request.POST.get('text_input')
            user_talk = userInput
            answer = translator.nyk_eng_translator(user_talk)
            messages.info(request, answer)
    return render(request, 'visualizer/index.html', {
       'TextInputForm':TextInputForm,
       'answer': answer,
    })

def signup_view(request):
    signup_form = forms.signup_form()
    show_create = False

    if request.method == 'POST':
        #if 'password_button' in request.POST:
        #    if signup_form.is_valid:
        #        print('$$$$$$$$$$$$')
        #        password = request.POST.get('Password')
        #        try:
        #            User(username=request.session['email'],email=request.session['email'],password=password)
        #            request.session.clear()
        #            login(request, request.user)
        #            messages.success(request, 'Loged in successfully')
        #            return HttpResponseRedirect(reverse('account'))
        #        except KeyError:
        #            return HttpResponseRedirect(reverse('signup'))

        signup_form = forms.signup_form(request.POST)
        if  signup_form.is_valid:
            email = request.POST.get('email')
            request.session['email'] = email

            ##############################
            ####### User.objects.get_or_create()
            try:
                qs = User.objects.get(email = email)
                if qs:
                    messages.info(request, '''This email is in use to DS account!''')
                
            except User.DoesNotExist:
                show_create = True
                #system_pass=generate_password()
                ############################
                #####SEND AN EMAIL HERE#####
                messages.success(request, '''Create your password''')
                return render(request, 'visualizer/signup.html', {
                    'signup_form':signup_form,
                    'show_create':show_create,
                })
            except User.MultipleObjectsReturned:
                messages.warning(request, '''You already 
                    have an account related to this email!''')
            return HttpResponseRedirect(reverse('signup'))
        
        
    #if reques.GET:
    #passwd = request.GET.get('xfz233')
    #   
    #    if passwd == system_pass:
    #        user = User.objects.create(Username = email, email = email)
    #        user.save()
    #    else:
    #        messages.warning(request, '''Something went wrong,
    #          Please try again!''')
            
    return render(request, 'visualizer/signup.html', {
        'signup_form':signup_form,
        'show_create':show_create,
    })

def signin_vew(request):
    TextInputForm = forms.TextInputForm()
    if request.user.is_authenticated and not(request.user.is_anonymous):
        if request.user.is_staff:
            return HttpResponseRedirect(reverse('admin_account'))
        else:
            return HttpResponseRedirect(reverse('account'))
    if request.method == 'POST':
        TextInputForm = forms.TextInputForm(request.POST)
        if  TextInputForm.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = authenticate(username = email, password = password)
                if user is not None:
                    login(request, user)
                    if request.user.is_staff:
                        messages.success(request, 'Loged in successfully')
                        return HttpResponseRedirect(reverse('admin_account'))
                    else:
                        messages.success(request, 'Loged in successfully')
                        return HttpResponseRedirect(reverse('account'))
                else:
                    messages.warning(request, 'Wrong username or password!')
                    return HttpResponseRedirect(reverse('signin'))
            except user.PermmisionDeniedError:
                pass
            
    return render(request, 'visualizer/signin.html', {
        'TextInputForm':TextInputForm,
    })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
