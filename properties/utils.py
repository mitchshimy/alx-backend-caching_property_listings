from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Retrieve all properties from the cache if available,
    else fetch from DB and store in cache for 1 hour.
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all().values('title', 'description', 'price', 'location', 'created_at'))
        cache.set('all_properties', properties, timeout=3600)  # cache for 1 hour
    return properties
