from django.urls import path
from . import views, AdminViews, StudentViews, TeacherViews
urlpatterns = [
    # Login Path
    path('', views.home, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register , name="register")
    # Student Path
    # Teacher Path 
    # Admin Path
]