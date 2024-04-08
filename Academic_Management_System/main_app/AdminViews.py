from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from django.urls import reverse
# from database import Student, Teacher, Course
def home(request):
  return render(request,'Manager/home.html')
def student_view(request):
  return render(request,'Manager/student.html',{
     'List':None
  })
def teacher_view(request):
  return render(request,'Manager/teacher.html',{
    'List':None
  })
def course_view(request):
  return render(request,'Manager/course.html',{
    'List':None
  })
def notification_view(request):
  return render(request,'Manager/notification.html')
def feedback_view(request):
  return render(request,'Manager/feedback.html')
def stdinfo(request, id):
  pass
def addstd(request):
  return render(request,'Manager/addstd.html',{
     'message':None
  })
def doAddStd(request):
 pass
def doDelStd(request, id):
  pass


