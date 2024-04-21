from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from Database import Student, Course, Class, Content

def login_required(func):
  def wrapper(request, *args, **kwargs):
    if 'student_id' not in request.session or request.session['login'] == False:
      return redirect('login')
    else:
      return func(request, *args, **kwargs)
  return wrapper
@login_required
def student_home(request):
      return render(request, 'Student/home.html',{
          'student':Student.get_student(request.session['student_id'])
      })
@login_required
def tkb(request):
      tkb = Student.get_timetable(request.session['student_id'])
      return render(request, 'Student/tkb.html',{
          'TKB':None if tkb == None else tkb['List'],
          'Count':0 if tkb == None else len(tkb['List']),
          'Credits':0 if tkb == None else tkb['Credits']
      })
def register(request):
    print(Student.get_course(request.session['student_id']))
    return render(request, 'Student/register.html',{
       'default' : True,
       'course_list': Student.get_course(request.session['student_id'])
    })
def search(request):
    return render(request,'Student/register.html',{
      'default' : False,
      'course':Course.getCourse(request.GET['course_id']),
      'class': Class.all(request.GET['course_id']),
      'course_list': Student.get_course(request.session['student_id'])
    })
def delCourse(request,course_id,class_id):
    Student.delete_course(request.session['student_id'],course_id, class_id)
    return HttpResponseRedirect(reverse(register))
@login_required
def course(request):
    tkb = Student.get_timetable(request.session['student_id'])
    print(tkb)
    return render(request,'Student/course.html',{
        'courses': None if tkb == None else tkb['List']
    })
@login_required
def result(request):
    return render(request, 'Student/result.html',{
        'Result': Student.get_result(request.session['student_id']) if Student.get_result(request.session['student_id']) != None else None,
        'Student':Student.get_student(request.session['student_id']) if Student.get_student(request.session['student_id']) != None else None
    })
def register_course(request,course_id,class_id):
   if Student.register_course(request.session['student_id'],course_id,class_id):
       return HttpResponseRedirect(reverse(register))
   else:
       return HttpResponseRedirect(reverse(register))
def content_student(request, course_id, class_id):
    return render(request,'Student/content.html',{
        'Content':Content.load(course_id,class_id)
    })