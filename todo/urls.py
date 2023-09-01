from django.urls import path
from todo.views import TaskListAPIView, TaskDetailAPIView, CategoryListAPIView, CategoryDetailAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='task-list-api'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail-api'),
    path('category/', CategoryListAPIView.as_view(), name='category-list-api'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail-api')
]
