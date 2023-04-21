from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm,PasswordChangeForm,PasswordResetForm,_
from . models import Student
class StudentDetailsForm(forms.ModelForm):
    class Meta():
        model=Student
        fields=['first_name','last_name','email','phone']
        widgets={'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.TextInput(attrs={'class':'form-control'}),
                  'phone':forms.NumberInput(attrs={'class':'form-control'})
                }

class StudentRegistrationForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta():
        model=User
        fields=['username','email','password1','password2']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}



class MyPasswordResetForm(PasswordResetForm):
       email=forms.EmailField(label=_("Email"),max_length=200,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
    new_password2=forms.CharField(label=_("confirm New Password"),max_length=200,strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_("old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password2=forms.CharField(label=_("Confrim New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))