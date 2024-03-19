from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,'index.html')
def home(request):
  list = [1,2,3,4,5,6,7]
  return render(request,'base.html',{
     'List': list
     
  })