from django.shortcuts import render, render_to_response
#from botocore.vendored.requests.api import request
#from graphene.types.tests.test_resolver import context
from django.utils.lorem_ipsum import paragraph


# Create your views here.
def test(request):
    context = {
        'appname': __file__,
        'header': 'This is the test header',
        'paragraph': 'This is the test paragraph'
    }
    return render(request,'account/test.html',context)