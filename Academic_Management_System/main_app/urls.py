from django.urls import path
from . import views, AdminViews, StudentViews, TeacherViews
urlpatterns = [
    # Login Path
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('index', views.index, name="index"),
    path('register', views.register , name="register"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('doRegister',views.doRegister, name="doRegister"),
    # Student Path
    path('student_home', StudentViews.student_home, name="student_home"),
    path('tkb',StudentViews.tkb, name="tkb"),
    path("register_course", StudentViews.register, name="register_course"),
    path("course", StudentViews.course, name="course"),
    path("result",StudentViews.result, name = "result"),
    # Teacher Path 
    path('teacher_home', TeacherViews.teacher_home , name="teacher_home"),
    path('schedule', TeacherViews.schedule , name="schedule"),
    path('teacher_course', TeacherViews.course, name="teacher_course"),
    path('score',TeacherViews.score, name="score"),
    path('notification', TeacherViews.notification , name="notification"),
    # Admin Path
    path('admin_home', AdminViews.home, name="admin_home"),
    path('student_view', AdminViews.student_view, name="student_views"),
    path('teacher_view', AdminViews.teacher_view, name="teacher_views"),
    path('course_view', AdminViews.course_view, name="course_views"),
    path('notification_view', AdminViews.notification_view, name="notification_views"),
    path('feedback_view', AdminViews.feedback_view, name="feedback_views"),
    path('stdifo/<int:id>',AdminViews.stdinfo , name="stdinfo"),
    path('addstd',AdminViews.addstd, name="addstd"),
    path('doAddStd',AdminViews.doAddStd, name="doAddStd"),
    path('doDelStd/<int:id>',AdminViews.doDelStd, name="doDelStd"),
]