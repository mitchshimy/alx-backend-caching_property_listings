from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)  # Cache the view for 15 minutes
def property_list(request):
    properties = Property.objects.all().values('title', 'description', 'price', 'location', 'created_at')
    return JsonResponse({
        "data": list(properties)
    })
