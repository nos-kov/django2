from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher, Student

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {}
    context = {"object_list": Student.objects.all().order_by('name').values(),}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
