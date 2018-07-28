from django.conf.urls import url

from BBS import views

urlpatterns = [
    url(r'^index/', views.index),
]
