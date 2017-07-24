from django.conf.urls import url
from . import views
# from django.contrib import admin
from . import views
urlpatterns = [
        url(r'^$', views.index),
        url(r'^first_app/all.json$', views.all_json),
        url(r'^first_app/all.html$', views.all_html),
        url(r'^first_app/find$', views.find),
        url(r'^first_app/create$', views.create),

        ]
