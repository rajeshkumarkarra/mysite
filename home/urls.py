"""test2 URL Configuration

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
from django.urls import path
from home import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('about/',views.about,name='AboutUs'),
    path('itemPage/',views.blog_item,name='ItemPage'),
    path('blog/',views.blog,name='Blog'),
    #below  contact/ for to view contact form on the website
    path('contact/',views.contact,name='contact'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('service/',views.service,name='service'),
    # below contactform/ (from "form action in contact.html) (and id = contact in contact.html) is for whenever client submit his details in the contactform
    path('contactform/',views.contactform,name='contactform'),
    path('emailSubscribe/', views.contact, name='emailSubscribe'),
]

