from django.shortcuts import render, HttpResponseRedirect
def index(request):
  return render(request, 'Student/home.html');