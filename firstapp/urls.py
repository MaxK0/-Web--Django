#from django.urls import include, re_path

#from . import views

#from django.urls import path

#urlpatterns = [
  #  re_path('', views.index, name='index'),
   # re_path(r'^course/$', views.courseListView.as_view(), name='course'),
   # re_path(r'^course/(?P<pk>\d+)$', views.courseDetailView.as_view(), name='данные о курсе')
#
#]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/', views.courseListView.as_view(), name='course'),
    path('course/<int:pk>/', views.courseDetailView.as_view(), name='данные о курсе'),
    path('teacher/', views.teacherListView.as_view(), name='teacher'),
    path('teacher/<int:pk>/', views.teacherDetailView.as_view(), name='данные о преподавателе'),
]
