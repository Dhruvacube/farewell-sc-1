from django.conf import settings
from django.conf.urls import re_path
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', entry, name="Student Entry Page"),
    path('class/<slug:class_stu>',student_class_wise, name="Student Class Wise"),
    re_path(r'^search/$', search, name="Student Search Page"),
    
    path('profile/<slug:class_stu>/<slug:slug>', student, name="Student Profile"),
    path('addnickname/<slug:slug>', addnicknames, name="Add Nickname"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
