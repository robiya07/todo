from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from apps.views import CustomLoginView, RegisterPageView, MainView, TaskDetailView, TaskCreateView, TaskUpdateView, \
    TaskDeleteView

urlpatterns = [
    path('', MainView.as_view(), name='tasks'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register'),

    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),

    path('create-task/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]
