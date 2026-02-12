from django.urls import path
from .views import (
    ProjectListCreateView,
    ProjectDetailView,
    ProjectPlaceListCreateView,
    PlaceDetailView
)

urlpatterns = [
    # 1. Проєкти: Створення (POST) та Список (GET)
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),

    # 2. Проєкти: Деталі, Оновлення, Видалення
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    # 3. Місця в проєкті: Список місць конкретного проєкту (GET) та Додавання (POST)
    # Важливо: <int:project_pk> має співпадати з кодом у view
    path('projects/<int:project_pk>/places/', ProjectPlaceListCreateView.as_view(), name='project-places-list'),

    # 4. Конкретне місце: Деталі, Зміна нотатки/статусу, Видалення
    path('places/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
]