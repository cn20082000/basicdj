from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def hello(request):
    # text = """<h1>Welcome to my app!</h1>"""
    # return HttpResponse(text)
    return render(request, "hello.html", {})

def welcome(request):
    return redirect('myapp/')