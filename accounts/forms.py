from string import Template

from django import forms
from django.core import validators
from django.forms import ImageField
from django.utils.safestring import mark_safe

from .models import Interest,Profile, User


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html = Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', ]


class ProfileView(forms.ModelForm):
    user_name=forms.CharField(validators=[validators.MinLengthValidator(3)])
    first_name=forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder":"optional"}))

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))

    YEARS = [x for x in range(1940, 2003)]
    birthdate = forms.DateField(initial="1994-06-21", widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = Profile
        fields = ["user_name","first_name", "last_name", "gender", "birthdate"]
    def clean(self):
        user_name=self.cleaned_data["user_name"]  
        if Profile.objects.filter(user_name=user_name).exists():
            raise forms.ValidationError("This username is already taken")
       


class ProfileView2(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))

    class Meta:
        model = Profile
        fields = ["profile_image", "bio"]

class InterestView(forms.ModelForm):
    try:
        choices = [(topic.id,topic.interest) for topic in Interest.objects.all()]
    except:
        choices = []
    interest = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=choices)
    class Meta:
        model = Profile
        fields = ["interest"]


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))

    bio = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))
    YEARS = [x for x in range(1940, 2003)]
    birthdate = forms.DateField(initial="1994-06-21", widget=forms.SelectDateWidget(years=YEARS))
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'gender',
                  'profile_image', 'bio', 'account_type', 'birthdate','interest']
