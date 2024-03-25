from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

def home(request):
  return render(request,'Manager/home.html')
def student_view(request):
  return render(request,'Manager/student.html')
def teacher_view(request):
  return render(request,'Manager/teacher.html')
def course_view(request):
  return render(request,'Manager/course.html')
def notification_view(request):
  return render(request,'Manager/notification.html')
def feedback_view(request):
  return render(request,'Manager/feedback.html')