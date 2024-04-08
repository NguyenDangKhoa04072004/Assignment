from django.shortcuts import render, HttpResponseRedirect
def student_home(request):
  return render(request, 'Student/home.html')
def tkb(request):
  return render(request, 'Student/tkb.html')
def register(request):
  return render(request, 'Student/register.html')
def course(request):
  return render(request,'Student/course.html')
def result(request):
  return render(request, 'Student/result.html')