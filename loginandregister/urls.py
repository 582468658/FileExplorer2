"""loginandregister URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^login/',views.login),
    url(r'^register/',views.register),
    url(r'^change_pwd/', views.change_pwd),
    #url(r'mainpage/', login_required(views.list1)),
    #url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    url(r'^create_code_img/', views.create_code_img),
    url(r'^addblog/', views.addblog),
]
