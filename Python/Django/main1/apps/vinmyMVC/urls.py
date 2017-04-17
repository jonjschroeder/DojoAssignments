from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^users$', views.show),
    url(r'^aboutme$', views.aboutme),
    url(r'^projects$', views.projects),
    url(r'^new_user$', views.create),
    url(r'^gen$', views.gen),
    url(r'^back$', views.back),
    # url(r'^farm$', views.farm),
    url(r'^all$', views.all),



]
