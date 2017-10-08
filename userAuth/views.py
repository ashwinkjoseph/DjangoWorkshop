from django.shortcuts import redirect, render
from .forms import LoginForm, SignUpForm
# from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def logins(request):
    print(request.POST)
    if request.method == "POST":
        #task when user submits login credentials
        form = LoginForm(request.POST)
        if form.is_valid():
            #form_contents = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home_page', user.pk)
            else:
                print('here')
        else:
            print('im here')
            print(form.errors)
    else:
        #logic for giving form for users to fill etc
        form = LoginForm()
        return render(request, 'userAuth/login.html', {
            'form': form,
            "status": 0
        })

def signup(request):
    if request.method == "POST":
        form_contents = SignUpForm(request.POST)
        if form_contents.is_valid():
            form = form_contents.save(commit=False)
            password = form.password
            form.set_password(password)            
            form.save()
            return redirect('login_page')
        else:
            form = SignUpForm()
            return render(request, 'userAuth/signup.html', {
                'form': form,
                'status': 1
            })
    else: 
        form = SignUpForm()
        return render(request, 'userAuth/signup.html', {
            'form': form,
            'status': 0
        })