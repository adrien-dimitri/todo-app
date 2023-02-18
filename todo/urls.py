from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'todo'
urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='todo:login'), name='logout'),

    path('', views.TaskList.as_view(), name='index'),

    path('task/<int:pk>/', views.TaskDetail.as_view(), name='detail'),

    path('edit/<int:pk>/', views.TaskUpdate.as_view(), name='edit'),
    path('create/', views.TaskCreate.as_view(), name='create'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='delete'),
]