from django.conf.urls import url
from . import views

app_name = 'question'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^paper/', views.paper, name='paper'),
    url(r'^select_subjects/', views.select_subjects, name='select_subjects'),
    url(r'^select_unit/', views.select_unit, name='select_unit'),
    url(r'^select_question/', views.select_question, name='select_question'),


    # url(r'^paper1.pdf$', views.pdf),
]