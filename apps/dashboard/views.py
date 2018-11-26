from django.shortcuts import render

# Create your views here.
def load_dashboard(request):
    return render(request,'dashboard/index.html')