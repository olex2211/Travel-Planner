import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.exceptions import ValidationError

def validate_art_place(external_id):
    """
    NOTE: In a high-load production environment, this should be handled 
    asynchronously to avoid blocking the main thread. 
    For this assessment, synchronous requests are used for simplicity.
    """
    cache_key = f"art_place_exists_{external_id}"
    
    if cache.get(cache_key):
        return True
    
    api_url = getattr(settings, 'ART_API_URL',)
    url = f"{api_url}/{external_id}"

    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 404:
            raise ValidationError(f"Place with ID {external_id} not found in Art Institute API.")
        
        if response.status_code != 200:
            raise ValidationError(f"External API error: {response.status_code}")
        
        cache.set(cache_key, True, timeout=60*60*24)  # 24 hours cache
        return True

    except requests.RequestException:
        raise ValidationError("Failed to connect to Art Institute API.")