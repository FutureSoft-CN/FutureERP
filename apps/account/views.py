from django.shortcuts import render, render_to_response, redirect
from django.utils.lorem_ipsum import paragraph

from django.contrib import auth
from apps.account.forms import LoginForm

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from FutureERP import settings

# Create your views here.
def test(request):
    context = {
        'appname': __file__,
        'header': 'This is the test header',
        'paragraph': 'This is the test paragraph'
    }
    return render(request,'account/test.html',context)

def test_redirect(request):
#    return HttpResponse("ok")
    return redirect('/dashboard/')

def login(request):
    if request.method=='POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():                
            user = auth.authenticate(username=forms.cleaned_data['username'],password=forms.cleaned_data['password'])             
            if user is not None and user.is_active:
                auth.login(request, user)
                print('Output from',__file__,'logged in succesfully!')
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                return render(request, 'account/login.html',{'status':'ERROR Incorrect username or password'})    
        else:
            return render(request, 'account/login.html',{'status':'ERROR Incorrect username or password'})
    else:
        return render(request,'account/login.html')
  
@login_required
def logout(request): 
#    return HttpResponse("You're logged out.")  
    print('Output from',__file__,'logged out succesfully!')
    auth.logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)    

def register(request): 
    if request.method == 'POST':
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            new_user = forms.save()
            return redirect('/dashboard/index.html')
    else:
        forms = UserCreationForm()
    return render_to_response("registration/register.html", {
        'forms': forms,
    })
    