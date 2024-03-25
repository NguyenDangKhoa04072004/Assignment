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
    # Teacher Path 
    # Admin Path
    path('admin_home', AdminViews.home, name="admin_home"),
    path('student_view', AdminViews.student_view, name="student_views"),
    path('teacher_view', AdminViews.teacher_view, name="teacher_views"),
    path('course_view', AdminViews.course_view, name="course_views"),
    path('notification_view', AdminViews.notification_view, name="notification_views"),
    path('feedback_view', AdminViews.feedback_view, name="feedback_views"),
]