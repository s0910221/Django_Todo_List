from django.urls import path

from . import views as v

app_name = 'todo'
urlpatterns = [
    path('', v.index, name = 'index'),
    path('new/', v.new, name = 'new'),
    path('edit/<int:pk>/', v.edit, name='edit'),
    path('delete/<int:pk>/', v.delete, name='delete'),
    path('<int:pk>/', v.show, name='show')
]
