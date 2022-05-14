from django.urls import path, re_path
from .views import *


urlpatterns = [
    
    re_path(r'^add/$', CartView.as_view()),
    re_path(r'^remove/$', CartRemoveView.as_view()),
    
]