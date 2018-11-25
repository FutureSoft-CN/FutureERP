from django.shortcuts import render, render_to_response
from botocore.vendored.requests.api import request
from graphene.types.tests.test_resolver import context
from django.utils.lorem_ipsum import paragraph


# Create your views here.
def test(request):
    context = {}
    context['appname']=__file__
    context['header']='This is the test header'
    context['paragraph']='This is the test paragraph'
    return render(request,'account/test.html',context)