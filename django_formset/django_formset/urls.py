"""django_formset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from exams import views as exam_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^exams/dashboard/', exam_views.dashboard.as_view(), name = 'exam_dashboard' ),
    url(r'^exams/add/', exam_views.exam_add , name = 'exam_add'),
    url(r'^exams/(?P<pk>\d+)/edit/', exam_views.exam_edit , name = 'exam_edit'),
    url(r'^exams/getset/', exam_views.getset , name = 'getset'),

]
