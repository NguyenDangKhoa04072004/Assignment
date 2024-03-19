from django.urls import path
from . import views, AdminViews, StudentViews, TeacherViews
urlpatterns = [
    # Login Path
    path('', views.index, name="index"),
    path('home', views.home , name='home')
    # Student Path
    # Teacher Path 
    # Admin Path
]