"""netmag URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from blog.views import *
urlpatterns = [
    path('music/', include('music.urls')),
    path('admin/', admin.site.urls),
    path('blog/',first_view,name = 'home'),
    path("blog_reverse_url/<int:post_id>",detail_view,name = 'detail'),
    path('blog/create',post_create_view,name = 'create'),
    path('blog/upload',upload_view,name=  'upload'),
    path('blog/database',file_view,name=  'file_view')
]
