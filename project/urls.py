"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from spm import views as spm_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', spm_view.users_view, name= 'spmuser'),
    path('register/', user_views.register, name= 'register'),
    path('student/', user_views.student, name= 'student'),
    path('faculty/', user_views.faculty, name= 'faculty'),
    path('depthead/', user_views.department_head, name= 'depthead'),
    path('registrarsofc/', user_views.registrars_office, name= 'registrarsofc'),
    path('vc/', user_views.vc, name= 'vc'),
    path('dean/', user_views.dean, name= 'dean'),
    path('department/', user_views.department, name= 'department'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('spm.urls')),
]
