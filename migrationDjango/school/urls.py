from django.urls import path
from django.contrib import admin
from school.views import students_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', students_list, name='students'),
]
