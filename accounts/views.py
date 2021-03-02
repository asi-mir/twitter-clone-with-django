from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import User
from django.urls import reverse_lazy, reverse
from . import forms
from . import token



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
                random_token = token.get_random_token()
                print(random_token)
                user.token = random_token
                user.save()
                request.session['user_phone'] = user.phone
                return redirect("accounts:verify")

        except User.DoesNotExist:
            print('does not exists')
            form = forms.SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                random_token = token.get_random_token()
                print(random_token)
                user.token = random_token
                user.is_active = False
                user.save()
                request.session['user_phone'] = user.phone
                request.session['register_user'] = True
                return redirect("accounts:verify")

        return render(request, self.template_name,{"form":self.form_class})



class VerifyTokenView(View):    

    def get(self,request,*args,**kwargs):   
        try:        
            phone = request.session.get('user_phone')   
            return render(request, 'verify.html', {'phone': phone})
        except User.DoesNotExist:
            return redirect("accounts:signup")

    def post(self,request):
        phone = request.session.get('user_phone')
        print(phone)
        user = User.objects.get(phone = phone) 
        if user.token != int(request.POST.get('token')):
            print("Token is incorrect.")
            return redirect("accounts:verify")

        user.is_active = True
        user.save()
        login(request, user)
        if request.session.get('register_user'):
            print('user registered')
        return redirect("accounts:home")
        