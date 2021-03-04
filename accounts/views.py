from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import User
from django.urls import reverse_lazy, reverse
from . import forms
from . import token
import hashlib,datetime


class HomeView(View):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self,request):
        logout(request)
        return redirect("accounts:signup")

class SignupView(View):
    form_class=forms.SignupForm
    template_name='register.html'

    def get(self,request,*args,**kwargs):       
        return render(request, self.template_name,{'form':self.form_class})

    def post(self,request):
        try:
            if "phone" in request.POST:
                phone = request.POST.get('phone')
                user = User.objects.get(phone=phone)
                random_token,salt,expiration_date = token.generate_token()
                user.token = random_token
                user.salt = salt
                user.token_expiration_date = expiration_date
                print(user.token_expiration_date)
                user.save()
                request.session['user_phone'] = user.phone
                request.session['token_expiration'] = str(user.token_expiration_date)
                return redirect("accounts:verify")

        except User.DoesNotExist:
            print('does not exists')
            form = forms.SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                random_token,salt,expiration_date = token.generate_token()
                print(expiration_date)
                user.token = random_token
                user.salt = salt
                user.token_expiration_date= expiration_date
                user.is_active = False
                user.save()
                request.session['user_phone'] = user.phone
                request.session['token_expiration'] = str(user.token_expiration_date)
                request.session['register_user'] = True
                return redirect("accounts:verify")

        return render(request, self.template_name,{"form":self.form_class})



class VerifyTokenView(View):    

    def get(self,request,*args,**kwargs):   
        try:        
            phone = request.session.get('user_phone')  
            token_expiration = request.session.get('token_expiration')
            print(token_expiration)
            print(datetime.datetime.now())
            expiration_date = datetime.datetime.strptime(token_expiration, '%Y-%m-%d %H:%M:%S.%f') 
            if expiration_date < datetime.datetime.now():
                user = User.objects.get(phone=phone)
                random_token,salt,expiration_date = token.generate_token()
                print(expiration_date)
                user.token = random_token
                user.salt = salt
                user.token_expiration_date= expiration_date
            expr = str(expiration_date.month) + '/' + str(expiration_date.day) + '/' + str(expiration_date.year) + ' ' + str(expiration_date.hour) + ':' + str(expiration_date.minute) + ':' + str(expiration_date.second)
           
            return render(request, 'verify.html', {'phone': phone,'expiration_date':expr})
        except User.DoesNotExist:
            return redirect("accounts:signup")

    def post(self,request):
        phone = request.session.get('user_phone')
        print(phone)
        user = User.objects.get(phone = phone) 
        entry_hash_token = hashlib.sha256((request.POST.get('token')+user.salt).encode('utf-8')).hexdigest()
        if entry_hash_token != user.token:
            print("Token is incorrect.")
            return redirect("accounts:verify")
        if user.token_expiration_date < datetime.datetime.now():
            print("This token is expired")
            return redirect("accounts:verify")
        user.is_active = True
        user.save()
        login(request, user)
        if request.session.get('register_user'):
            print('user registered')
        return redirect("accounts:home")
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("accounts:signup")