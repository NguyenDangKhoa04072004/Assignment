from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from Database import User, Student, Teacher, Message
# Create your views here.
def logout_required(func):
  def wrapper(request,*args,**kwargs):
    if 'student_id' in request.session and 'teacher_id' in request.session:
      del request.session['student_id']
      del request.session['teacher_id']
      del request.session['login']
      return redirect('home')
    if 'student_id' in request.session and request.session['login'] == True:
      return redirect('student_home')
    elif 'teacher_id' in request.session and request.session['login'] == True:
      return redirect("teacher_home")
    elif 'admin' in request.session and request.session['login'] == True:
      return redirect("admin_home")
    else:
      return func(request, *args, **kwargs)
  return wrapper
@logout_required
def home(request):
    return render(request,'home.html',{
      'Message':Message.all()
    })
@logout_required
def index(request):
    return render(request,'index.html')
@logout_required
def login(request):
    return render(request,'login.html',{
      'message':None
    })
def doLogin(request):
  if request.method == 'POST':
    user = User.Login(request.POST['email'], request.POST['password'])
    if user['Success']:
      if user['Type'] == 'Student':
        request.session["student_id"] = user['ID']
        request.session["login"] = True
        return redirect("student_home")
      else:
        request.session["teacher_id"] = user['ID']
        request.session["login"] = True
        return redirect("teacher_home")
    else:
     return render(request,'login.html',{
         'active':False,
         'message':user['Message']
      })
    
def AdminLogin(request):
  if request.method =='POST':
    message = User.AdminLogin(request.POST['email'],request.POST['password'])
    if message == None:
      request.session['admin'] = True
      request.session['login'] = True
      return redirect("admin_home")
    else:
      return render(request,'login.html',{
         'active':True,
         'message_admin':message
      })
def logout(request):
  request.session["login"] = False
  if "student_id" in request.session:
    del request.session["student_id"]
  if "teacher_id" in request.session:
    del request.session["teacher_id"]
  if 'admin' in request.session:
    del request.session['admin']
  print(request.session["login"])
  request.session.save()
  return redirect("home")

