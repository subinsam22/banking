from .models import District
def menu_district(request):
    district=District.objects.all()
    return dict(district=district)