from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from django.contrib import messages

#Modify in the built in User creation form of django 
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply Tailwind CSS classes to fields
        for field_name in ['username', 'email', 'password1', 'password2']:
            self.fields[field_name].widget.attrs.update({
                'class': 'block w-full rounded-md border border-gray-300 focus:border-purple-700 focus:outline-none focus:ring-1 focus:ring-purple-700 py-1 px-1.5 text-gray-500'
            })
############################################################


def login_user(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(request=req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('/')
        else:
            messages.error(req, 'There is an error in login try again buddy.')
            return render(req, 'auth/login.html')
    else:
        return render(req, 'auth/login.html', {})


def register_user(req):
    if req.method == "POST":
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('/')
        else:
            print(req.POST)
    else:
        form = CustomUserCreationForm()

    return render(req, 'auth/register.html', {'form': form})

@login_required
def logout_user(req):
    logout(req)
    return redirect('login')