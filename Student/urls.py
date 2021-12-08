"""Student URL Configuration

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
from django.urls import path
import Students.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Students.views.get_students),
    path('student/add', Students.views.add_student),
    path('student/<int:student_id>', Students.views.get_student, name='get-student')
   # path('filter-users/user', Students.views.filtred_users_by_username),
    #path('user/<int:user_id>', Students.views.get_user, name='get-user')
]