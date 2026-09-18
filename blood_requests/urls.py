from django.urls import path
from .views import (
    request_list,
    request_detail,
    request_create,
    request_edit,
    request_delete,
    my_requests
)

urlpatterns = [
    path('', request_list, name='request_list'),
    path('create/', request_create, name='request_create'),
    path('my/', my_requests, name='my_requests'),
    path('<int:pk>/', request_detail, name='request_detail'),
    path('<int:pk>/edit/', request_edit, name='request_edit'),
    path('<int:pk>/delete/', request_delete, name='request_delete'),
]