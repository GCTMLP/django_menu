from django.urls import include, re_path, path

from . import views

urlpatterns = [
    re_path(r'^', views.main, name='main'),
    re_path(r'^(\d+)', views.main, name='main')
]