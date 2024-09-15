from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListCreateView.as_view()),
    path('list/<str:uuid>/', views.ListCrudView.as_view()),
    path('list/<str:uuid>/tasks/', views.ListTasksView.as_view()),
    path('list/<str:uuid>/tasks/<int:task_pk>/', views.ListTasksCrudView.as_view()),
    # path('tasks/', views.TasksListView.as_view()),
    # path('tasks/<int:pk>/', views.TaskEditView.as_view())
]