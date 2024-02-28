# task_manager_project/urls.py

from django.urls import path, include



urlpatterns = [
    path('', include('task_manager_app.urls')),
    
    path('api/', include('rest_framework.urls')), 
]
