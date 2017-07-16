from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^list/$', views.comment_list, name="comment_list"),
    url(r'^(?P<pk>\d+)/activate/$', views.activate, name="activate"),
]
