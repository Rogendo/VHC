"""
projecttracker URL Configuration

"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path("", include("tracker.urls")),


]
# urlpatterns +=[re_path(r'^.*',TemplateView.as_view(template_name="tracker/index.html"))]