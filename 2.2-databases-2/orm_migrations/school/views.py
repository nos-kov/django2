from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher, Student, Link

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {}
    context = {"object_list": Student.objects.all().order_by('name').values(),}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

def add(request):

    student = Student.objects.create(name="test", group="test")
    teacher = Teacher.objects.create(name="test", subject="test")
    link = Link.objects.create(teacher_id="1", student_id="3")
    link = Link.objects.create(teacher_id="2", student_id="2")
    msg="done"
    return HttpResponse(msg)