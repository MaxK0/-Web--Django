from django.shortcuts import render

# Create your views here.
from .models import Course, Teacher, Faculty

def index(request):
    num_course=Course.objects.all().count()
    num_teacher=Teacher.objects.count()
    num_faculty=Teacher.objects.count()

    return render(request, 'index.html', context={'num_course': num_course, 'num_teacher': num_teacher, 'num_faculty': num_faculty})

from django.views import generic

class courseListView(generic.ListView):
    model = Course

class courseDetailView(generic.DetailView):
    model = Course

class teacherListView(generic.ListView):
    model = Teacher

class teacherDetailView(generic.DetailView):
    model = Teacher