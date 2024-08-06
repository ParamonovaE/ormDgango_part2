from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    object_list = Student.objects.all().order_by('group')
    template = 'school/students_list.html'
    context = {
        'object_list': object_list,
    }
    return render(request, template, context)
