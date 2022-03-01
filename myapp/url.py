from unicodedata import name
from django.urls import include, path
from myapp.views import hello

urlpatterns = [
    path('', hello, name = 'hello')
]