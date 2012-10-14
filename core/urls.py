
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic.base import TemplateView
from core import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name ='home.html'), name='core-home'),
    url(r'^about', TemplateView.as_view(template_name ='about.html'), name='core-about'),
    url(r'^experience', views.ExperienceView.as_view(), name='core-experience'),
    url(r'^contact$', views.ContactView.as_view(), name='core-contact'),

)
