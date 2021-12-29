from django.urls import path
from django.urls.resolvers import URLPattern
from .views import ListTodo, DetailTodo

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view())
]