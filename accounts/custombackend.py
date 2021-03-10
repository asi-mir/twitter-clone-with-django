from django.contrib.auth.backends import ModelBackend

from .models import User


class PhoneBackend(ModelBackend):
    def authenticate(self,request,username=None, password=None, **kwargs):
        phone = kwargs['phone']

        try:
            user = User.object.get(phone=phone)
        except User.DoesNotExist:
            pass
