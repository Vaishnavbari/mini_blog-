"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),


    #LOGIN page_view
    path('login/',views.loginpageview,name="login"),
    # RRGISTER USER
    path('registeruser/',views.registeruser,name="registeruser"),
    # HOME PAGE
    path("",views.home,name="home"),
    # ABOUT PAGE
    path('about/',views.about,name="about"),
    # ADD BLOG PAGE VIEW URL 
    path('add/',views.add,name="add"),
    # LOGIN VALIDATION 
    path("validaion/",views.loginview,name="loginview"),
    # LOGOUT VIEW
    path("logout/",views.logout_view,name="logout"),
    # BLOG POSTING 
    path("blogs/",views.blogs,name="blogs"),
    # delete blog 
    path("delete_blog/<int:id>",views.delete_blog,name="delete"),
     # update pageview
    path("update_blog/<int:pk>",views.updateview,name="update"),
    # cancel update url 
     path("cancel_update/",views.cancel,name="cancel"),
    # 404 error page View
    path("error404/",views.errorpage404,name="error404"),
    # 500 error page View
    path("error500/",views.errorpage500,name="error500"),


   
]
