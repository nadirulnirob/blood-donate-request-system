from django.urls import path
from .views import donor_list, donor_detail, donor_create, donor_edit, donor_delete

urlpatterns = [
    path('', donor_list, name='donor_list'),
    path('create/', donor_create, name='donor_create'),
    path('<int:pk>/', donor_detail, name='donor_detail'),
    path('<int:pk>/edit/', donor_edit, name='donor_edit'),
    path('<int:pk>/delete/', donor_delete, name='donor_delete'),
]