from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
  return render(request,'home.html')
def index(request):
  return render(request,'index.html')
def login(request):
  return render(request,'login.html')
def register(request):
  return render(request,'register.html')
def doLogin(request):
  pass
def doRegister(request):
  pass