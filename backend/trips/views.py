from rest_framework import generics, filters
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import TravelProject, Place
from .serializers import TravelProjectSerializer, PlaceSerializer
from .paginators import ProjectPagination

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer

    pagination_class = ProjectPagination 
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    filterset_fields = ['is_completed']
    ordering_fields = ['start_date', 'name', 'created_at']


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer

    def perform_destroy(self, instance):
        if instance.places.filter(is_visited=True).exists():
            raise ValidationError("Cannot delete project with visited places.")
        
        instance.delete()

class ProjectPlaceListCreateView(generics.ListCreateAPIView):
    serializer_class = PlaceSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    
    filterset_fields = ['is_visited']
    
    ordering_fields = ['external_id', 'is_visited']

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        get_object_or_404(TravelProject, pk=project_id)
        return Place.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = get_object_or_404(TravelProject, pk=project_id)

        if project.places.count() >= 10:
            raise ValidationError("Project cannot have more than 10 places.")

        serializer.save(project=project)


class PlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        if instance.is_visited:
            project = instance.project
            if not project.places.filter(is_visited=False).exists():
                project.is_completed = True
                project.save()