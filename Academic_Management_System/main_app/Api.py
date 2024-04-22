from django.shortcuts import render
from django.http import JsonResponse
from database import Student, Teacher
def check_id(request):
  if 'teacher_id' in request.session:
    return JsonResponse({'Type':'Teacher' , 'ID':request.session['teacher_id'], 'Name':Teacher.get_teacher(request.session['teacher_id'])['Name']},)
  elif 'student_id' in request.session:
    return JsonResponse({'Type':'Student' , 'ID':request.session['student_id'], 'Name':Student.get_student(request.session['student_id'])['Name']})
  else: 
    return JsonResponse({'Name':'Admin'})