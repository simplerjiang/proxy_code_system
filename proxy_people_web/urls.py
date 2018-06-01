"""proxy_people_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from main_app.views import *
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.conf import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^make_auth/$',make_auth,name='make_auth'),
    url(r'^change_bot_qq/$',change_bot_qq,name='change_bot_qq'),
    url(r'^$',RedirectView.as_view(pattern_name="make_auth")),
]

urlpatterns +=patterns('',
                        url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
                        url(r'^static/<?P<path>.*>$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
                       )