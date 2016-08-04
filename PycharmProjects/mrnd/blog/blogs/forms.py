from django import forms
from django.contrib.auth.models import User
from models import posts

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password']



class RegistrationForm(forms.Form):
     username=forms.CharField(max_length=30,label="username",required=True,error_messages={'invalid':'Username should be unique'})
     email=forms.EmailField(label="emailid",required=True)
     password1=forms.CharField(max_length=30,widget=forms.PasswordInput(),label="password",required=True)
     password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(), label="password(again)", required=True)

     def clean_username(self):
       u=self.cleaned_data['username']
       try:
         u=User.objects.get(username__exact=u)
       except User.DoesNotExist:
         return self.cleaned_data['username']
       raise forms.ValidationError("Username Already Exists . Please Try another name",code='invalid')

     def clean(self):
       p1=self.cleaned_data['password1']
       p2=self.cleaned_data['password2']
       if p1 is not None and p2 is not None:
          if p1 != p2:
            raise forms.ValidationError("Two passwords did not match")
          else:
             return self.cleaned_data
       else:
          raise forms.ValidationError("Both fields should match")
