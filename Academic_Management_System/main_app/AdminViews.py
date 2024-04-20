from django.shortcuts import render, HttpResponseRedirect, redirect
from datetime import datetime
from django.urls import reverse
from Database import Student, Teacher, Course, Class, Major
from datetime import datetime
def login_required(func):
  def wrapper(request, *args, **kwargs):
    if 'admin' not in request.session or request.session['login'] == False:
      return redirect('login')
    else:
      return func(request,*args, *kwargs)
  return wrapper
def home(request):
    return render(request,'Manager/home.html',{
       'Student': len(Student.all()) if Student.all() != None else 0,
       'Teacher': len(Teacher.all()) if Teacher.all() != None else 0,
       'Course': len(Teacher.all()) if Course.all() != None else 0,
    })
def student_view(request):
    return render(request,'Manager/student.html',{
      'List':Student.all()
    })
def teacher_view(request):
    return render(request,"Manager/teacher.html",context={
       'List':Teacher.all()
    })
def course_view(request):
    return render(request,'Manager/course.html',{
    'List':Course.all()
  })
def notification_view(request):
    return render(request,'Manager/notification.html',{
       'student_list':Student.all(),
       'teacher_list':Teacher.all()
    })
def feedback_view(request):
    return render(request,'Manager/feedback.html')
def stdinfo(request, id):
    return render(request,'Manager/stdinfo.html',{
      'student': Student.get_student(id)
    })
def editstd(request,id):
    n = datetime.now().year
    year = list(range(n,1999,-1))
    date = datetime.strptime(str(Student.get_student(id)['Date']),'%d/%m/%Y')
    format_date = datetime.strftime(date,'%Y-%m-%d')
    return render(request,'Manager/editstd.html',{
    'student':Student.get_student(id),
    'Date':format_date,
    'message':None,
    'Major': Major(),
    'Year':year
  })
def doEditStd(request,id):
    if request.method == 'POST':
      Student.update(
        id,
        request.POST['name'],
        request.POST['email'],
        request.POST['major'],
        request.POST['date'],
        request.POST['year']
      )
      return HttpResponseRedirect(reverse(student_view))
def addstd(request):
    n = datetime.now().year
    year = list(range(n,1999,-1))
    return render(request,'Manager/addstd.html',{
      'message':None,
      'Major': Major(),
      'Year':year
    })
def doAddStd(request):
    if request.method == 'POST':
      date = datetime.strptime(request.POST['date'],'%Y-%m-%d')
      format_date = date.strftime("%d/%m/%Y")
      message = Student.create(
          request.POST['id'],
          request.POST['name'],
          request.POST['email'],
          request.POST['major'],
          format_date,
          request.POST['year'],
          request.POST['password']
      )   
    if message == None:
      return HttpResponseRedirect(reverse(student_view))
    else:
      return  render(request,'Manager/addstd.html',{
          'message':message
      })
def doDelStd(request, id):
    Student.remove(id)
    return HttpResponseRedirect(reverse(student_view))
def teacherinfo(request,id):
  return render(request,'Manager/teacherinfo.html',{
     'teacher':Teacher.get_teacher(id)
  })
def addteacher(request):
    return render(request,'Manager/addteacher.html',{
      'message':None
    })
def doAddTeacher(request):
    if request.method == 'POST':
      message = Teacher.create(
          request.POST['id'],
          request.POST['name'],
          request.POST['email'],
          request.POST['level'],
          request.POST['field'],
        request.POST['password']
      ) 
      if message == None:
        return HttpResponseRedirect(reverse(teacher_view))
      else:
        return   render(request,'Manager/addteacher.html',{
            'message':message
        })
def editTeacher(request,id):
    return render(request,'Manager/editTeacher.html',{
      'teacher':Teacher.get_teacher(id)
    })
def doEditTeacher(request,id):
    if request.method == 'POST':
      Teacher.update(
          id,
          request.POST['name'],
          request.POST['email'],
          request.POST['level'],
          request.POST['field']
      )
      return HttpResponseRedirect(reverse(teacher_view))
def doDelTeacher(request, id):
    Teacher.remove(id)
    return HttpResponseRedirect(reverse(teacher_view))
def addCourse(request):
    return render(request,'Manager/addcourse.html',{
     'message':None
  })
def doAddCourse(request):
    if request.method =='POST':
      message = Course.create(
        request.POST['id'],
        request.POST['name'],
        request.POST['credits'],
        request.POST['type']
      )
      if message == None:
        return HttpResponseRedirect(reverse(course_view))
      else:
        return render(request,'Manager/addcourse.html',{
          'message':message
        }) 
def editCourse(request,id):
    return render(request,'Manager/editCourse.html',{
      'course':Course.getCourse(id)
    })
def doEditCourse(request,id):
    if request.method == 'POST':
      Course.update(
        id,
        request.POST['name'],
        request.POST['credits'],
         request.POST['type']
      )
      return HttpResponseRedirect(reverse(course_view))
def doDelCourse(request,id):
    Course.remove(id)
    return HttpResponseRedirect(reverse(course_view))
def courseinfo(request, course_id):
    course = Course.getCourse(course_id)
    return render(request,'Manager/courseinfo.html',{
      'course':course,
      'CLass_List':Class.all(course_id),
    })
def addclass(request, course_id):
    print(course_id)
    return render(request,'Manager/addclass.html',{
         'course_id':course_id,
         'message':None,
         'list_day':['2','3','4','5','6','7','CN']
    })
def doAddClass(request, course_id):
    if request.method == 'POST':
      message = Class.create(
        request.POST['class_id'],
       {
         'Building':request.POST['building'],
         'Room' : request.POST['room'],
         'Base': request.POST['base']
       },
       course_id,
       request.POST['teacher_id'],
       request.POST['maxsize'],
       {
         'Period': request.POST['period'],
         'Day': request.POST['day'],
         'Start':request.POST['Start'],
         'End':request.POST['End']
       },
      )
    if message ==None:
      return HttpResponseRedirect(reverse(courseinfo,kwargs={'course_id':course_id}))
    else:
      return render(request,'Manager/addclass.html',{
         'course_id':course_id,
         'message':message,
         'list_day':['2','3','4','5','6','7','CN']
      })
def editClass(request, course_id, class_id):
   return render(request,'Manager/editClass.html',{
     'class':Class.get_class(course_id,class_id),
     'course_id':course_id,
     'list_day':['2','3','4','5','6','7','CN']
  })
def doDelClass(request, course_id,class_id):
    Class.remove(course_id,class_id)
    return HttpResponseRedirect(reverse(courseinfo,kwargs={'course_id':course_id}))
def doEditClass(request, course_id, class_id):
   Class.update(
       course_id,
        class_id,
       {
         'Building':request.POST['building'],
         'Room' : request.POST['room'],
         'Base': request.POST['base']
       },
       request.POST['teacher_id'],
       request.POST['maxsize'],
       {
         'Period': request.POST['period'],
         'Day': request.POST['day'],
         'Start':request.POST['Start'],
         'End':request.POST['End']
       },
   )
   return HttpResponseRedirect(reverse(courseinfo,kwargs={'course_id':course_id}))