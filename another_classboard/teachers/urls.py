from django.urls import path
from .views import view_teachers

app_name = 'teachers'

urlpatterns =[
    path('', view_teachers, name='view_teachers'),
    path('<int:pk>/', view_teachers, name='view_teacher'),
    path('create/', view_teachers, name='view_teacher'),
]