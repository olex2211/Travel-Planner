from rest_framework import serializers
from .models import TravelProject, Place
from .services import validate_art_place
from django.db import transaction

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'external_id', 'notes', 'is_visited']
        read_only_fields = ['id']

    def validate_external_id(self, value):
        validate_art_place(value)
        return value


class TravelProjectSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, required=False)

    class Meta:
        model = TravelProject
        fields = ['id', 'name', 'description', 'start_date', 'is_completed', 'places']
        read_only_fields = ['id', 'is_completed']

    def validate(self, attrs):
        places = attrs.get('places', [])

        if len(places) >= 10:
            raise serializers.ValidationError({
                "places": "A project cannot have more than 10 places."
            })

        external_ids = [place['external_id'] for place in places]
        if len(external_ids) != len(set(external_ids)):
            raise serializers.ValidationError({
                "places": "Duplicate places (same external_id) are not allowed in one project."
            })

        return attrs

    def create(self, validated_data):
        places_data = validated_data.pop('places', [])

        with transaction.atomic():
            project = TravelProject.objects.create(**validated_data)
            
            for place_data in places_data:
                Place.objects.create(project=project, **place_data)
                
        return project