from django import forms
# from cryptography.fernet import Fernet
from maxx.models import *

class contactform(forms.ModelForm):
    first_name= forms.CharField(max_length=255)
    last_name= forms.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    message = forms.CharField(max_length=255)

    class Meta:
        model = contactmodel
        fields=['first_name','last_name','email','message']

class ProfileForm(forms.ModelForm):
    fname= forms.CharField(max_length=255)
    lname= forms.CharField(max_length=255)
    email = forms.EmailField(required=True,)
    password = forms.CharField(max_length=250)
    message = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields=['fname','lname','number','email', 'username', 'password']

class test(forms.ModelForm):
    name= forms.CharField(max_length=255)
    occupation = forms.CharField(max_length=255)
    class Meta:
        model = new
        fields=['name','occupation']

class Profile1Form(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=250)



# class upload_forms(forms.ModelForm):
#     class Meta:
#         model=upload
#         fields=['Artist_Name','Art_Description','Type','ArtWork','Price']

class upload_forms(forms.ModelForm):
    class Meta:
        model=upload_images
        fields=['Artist_Name','Art_Description','Type','ArtWork','Price']
