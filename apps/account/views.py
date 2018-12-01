from django.shortcuts import render, render_to_response, redirect
from django.utils.lorem_ipsum import paragraph

from apps.dashboard.views import load_dashboard
from django.contrib import auth


from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def test(request):
    context = {
        'appname': __file__,
        'header': 'This is the test header',
        'paragraph': 'This is the test paragraph'
    }
    return render(request,'account/test.html',context)

def test_redirect(request):
    return HttpResponse("ok")
    return redirect('/dashboard/')

def login(request):
    if request.method=='POST':
        
        input_uname = request.POST.get('username','')
        input_pwd = request.POST.get('password','')       
        user = auth.authenticate(username=input_uname,password=input_pwd)             
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect(request, '/dashboard/index.html')
        else:
            return render(request, 'account/login.html',{'status':'ERROR Incorrect username or password'})    
 
    return render(request,'account/login.html')
  
@login_required
def logout(request): 
    auth.logout(request)
    return HttpResponse("You're logged out.")     

def register(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('/dashboard/index.html')
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    })
    