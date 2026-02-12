from django.urls import path, include

urlpatterns = [
    path('trips/', include('trips.urls')), 
]