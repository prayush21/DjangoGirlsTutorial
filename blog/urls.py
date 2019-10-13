from django.urls import path, include
from . import views

urlpatterns = [
path('',views.post_list,name='post_list'),
path('post_new',views.post_new,name='post_new'),]
