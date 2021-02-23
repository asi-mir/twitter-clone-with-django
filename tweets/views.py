import abc
from intweet.settings import ALLOWED_HOSTS
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
import random
from django.conf import settings
from .models import Tweet
from .forms import TweetForm
from django.utils.http import is_safe_url

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.
def home_view(request,*args,**kwargs):
    print(request.user)
    return render(request,"pages/home.html",context={},status=200)
def tweet_list_view(request,*args,**kwargs):
    qs = Tweet.objects.all()
    tweet_list= [x.serialize() for x in qs]
    data ={
        "isUser":False,
        "response":tweet_list
    }
    return JsonResponse(data)
def tweet_detail_view(request,tweet_id,*args,**kwargs):
    """
    REST API VIEW
    CONSUME BY JS/SWIFT/JAVA/IOS/ANDROID
    RETURN JSON DATA
    """
    print(args,kwargs)
    data = {
        "id":tweet_id,
        #"image_path":obj.image.url
        #"restriction":obj.restriction
    }
    try:
        obj = Tweet.objects.get(id = tweet_id)
        data["content"] = obj.content
        status = 200
    except:
        data["message"]="Not Found"
        status = 404

    return JsonResponse(data,status=status)

def tweet_create_view(request,*args,**kwargs):
    if not request.user.is_authenticated:
        if request.is_ajax():
            return JsonResponse({},status=401)#401=Not authorized
        return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    

    if form.is_valid():
        obj=form.save(commit=False)
        obj.user = request.user
        obj.save()

        if request.is_ajax():
            return JsonResponse(obj.serialize(),status=201) #201==created item

        if next_url !=None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        return JsonResponse(form.errors,status=400)#400=bad request
    return render(request,'components/form.html',context={"form":form})