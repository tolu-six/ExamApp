from django.urls import path

from .views import AssignmentCreateView


urlpatterns = [
    path('create', AssignmentCreateView.as_view(), name='assignment-create'),
]
