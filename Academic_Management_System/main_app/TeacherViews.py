from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from Database import Teacher, Class, Course, Class, Content
def login_required(func):
    def wrapper(request, *args, **kwargs):
      if 'teacher_id' not in request.session or ("login" not in request.session or request.session["login"] == False):
         return redirect('login')
      else:
         return func(request, *args, *kwargs)
    return wrapper
@login_required
def teacher_home(request):
      return render(request,'Teacher/home.html',{
         'teacher':Teacher.get_teacher(request.session['teacher_id'])
      })
@login_required
def schedule(request):
      return render(request,'Teacher/schedule.html',{
           'Schedule':Teacher.get_schedule(request.session['teacher_id'])
      })
@login_required
def course(request):
      return render(request, 'Teacher/course.html',{
           'course':Teacher.get_schedule(request.session['teacher_id']),
           'Teacher': Teacher.get_teacher(request.session['teacher_id'])
      })
@login_required
def score(request):
      return render(request,'Teacher/score.html',{
           'course':Teacher.get_schedule(request.session['teacher_id']),
           'Teacher': Teacher.get_teacher(request.session['teacher_id'])
      })
@login_required
def notification(request):
      return render(request,'Teacher/notification.html',{
           'course':Teacher.get_schedule(request.session['teacher_id']),
           'Teacher': Teacher.get_teacher(request.session['teacher_id'])
      })
def notiList(request,course_id, class_id):
     return render(request,'Teacher/notiList.html',{
          'student_list':Class.get_studentList(course_id,class_id),
          'Course':course_id,
          'Class':class_id,
          'course':Course.getCourse(course_id),
          'class':Class.get_class(course_id,class_id)
     })
def studentList(request, course_id, class_id):
     return render(request,'Teacher/studentList.html',{
          'student_list':Class.get_studentList(course_id,class_id),
          'Course':course_id,
          'Class':class_id,
          'course':Course.getCourse(course_id),
          'class':Class.get_class(course_id,class_id)
     })
def scoring(request, student_id, course_id, class_id):
     if request.method =='POST':
            Teacher.scoring(student_id,course_id,
                                request.POST['excercise'],
                                request.POST['assignment'],
                                request.POST['midterm'],
                                request.POST['finalterm']
                            )
            return HttpResponseRedirect(reverse(studentList,kwargs={'class_id':class_id, 'course_id':course_id}))
     
def content(request, course_id, class_id):
     return render(request,'Teacher/content.html',{
          'Course':course_id,
          'Class':class_id,
          'Content':Content.load(course_id,class_id),
     })
def upload(request,course_id,class_id,subject):
     if request.method == 'POST':
          upload_file = request.FILES['file']
          Content.upload(course_id,class_id,subject,request.POST['title'],upload_file)
     return HttpResponseRedirect(reverse(content,kwargs={'course_id':course_id, 'class_id':class_id}))
def addsubject(request,course_id,class_id):
     Content.addSubject(course_id,class_id,request.GET['subject'])
     return HttpResponseRedirect(reverse(content,kwargs={'course_id':course_id, 'class_id':class_id}))
def delContent(request,course_id,class_id,subject,index):
     Content.delContent(course_id,class_id,subject,index)
     return HttpResponseRedirect(reverse(content,kwargs={'course_id':course_id, 'class_id':class_id}))