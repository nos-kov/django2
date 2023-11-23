from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher, Student

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {}
    context = {"object_list": Teacher.objects.all().order_by('name'),}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

def add(request):

    student = Student.objects.create(name="Иванов", group="1К")
    student = Student.objects.create(name="Трофимов", group="1Б")
    student = Student.objects.create(name="Калинин", group="1А")
    teacher = Teacher.objects.create(name="Петров", subject="Математика")
    teacher = Teacher.objects.create(name="Сидоров", subject="Русский")
    teacher = Teacher.objects.create(name="Гришин", subject="Информатика")
    msg="done"
    return HttpResponse(msg)
