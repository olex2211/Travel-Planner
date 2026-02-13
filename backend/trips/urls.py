from django.urls import path
from .views import (
    ProjectListCreateView,
    ProjectDetailView,
    ProjectPlaceListCreateView,
    PlaceDetailView
)

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),

    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    path('projects/<int:project_pk>/places/', ProjectPlaceListCreateView.as_view(), name='project-places-list'),

    path('places/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
]