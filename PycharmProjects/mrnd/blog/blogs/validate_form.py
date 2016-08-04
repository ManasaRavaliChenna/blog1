from .models import posts
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from forms import UserForm,LoginForm,RegistrationForm



class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login')

        return render(request, self.template_name, {'form': form})



class UserLogin(View):
     form_class = LoginForm
     template_name = 'registration/login.html'

     def get(self, request):
         form = self.form_class(None)
         return render(request, self.template_name, {'form': form})

     def post(self, request):
         form = self.form_class(request.POST)
         logout(request)
         username = password = ''
         if form.is_valid():
             user = form.save(commit=False)
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']

             user = authenticate(username=username, password=password)
             if user is not None:
                login(request, user)
                return redirect('list_posts')
             else:
                 redirect('register')

         return render(request, self.template_name, {'form': form})


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('list_posts')
        else:
            redirect('register')




def logout_view(request):
    logout(request)
    return redirect('list_posts')



def get_registrationform(request):
     if(request.method=='POST'):
        form=RegistrationForm(request.POST)
        if form.is_valid():
           username=form.cleaned_data['username']
           email=form.cleaned_data['email']
           password1=form.cleaned_data['password1']
           password2=form.cleaned_data['password2']
           if password1==password2:
              User.objects.create_superuser(username,email,password1)
              return redirect("login")
     else:
        form = RegistrationForm()
        return render(request,'registration/register.html',{'form':form})

