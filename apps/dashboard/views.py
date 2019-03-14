from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def load_dashboard(request):   
    return render(request,'dashboard.html')
    
    