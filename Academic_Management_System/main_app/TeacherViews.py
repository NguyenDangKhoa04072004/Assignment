from django.shortcuts import render, HttpResponseRedirect
def teacher_home(request):
  return render(request,'Teacher/home.html')
def schedule(request):
  return render(request,'Teacher/schedule.html')
def course(request):
  return render(request, 'Teacher/course.html')