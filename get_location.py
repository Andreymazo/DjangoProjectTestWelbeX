from django.shortcuts import render
from geopy.geocoders import Nominatim

from cargo.models import Cargo


def show_location_byuniknumber(request):
    zip = input(str('vvedite nomer gruza  '))
    f = Cargo.objects.all().get(unik_number=zip)
    print(f)
    ff = f.latitude_delivery
    fff = f.longtitude_delivery
    geolocator = Nominatim(user_agent="config")
    location_deliveri = geolocator.reverse(f"{ff}, {fff}")
    print(location_deliveri)

    ffff = f.latitude_pick_up
    fffff = f.longtitude_pick_up
    location_pick_up = geolocator.reverse(f"{ffff}, {fffff}")
    return render(request, 'cargo/location_bynumber.html', {'location_deliveri': location_deliveri,
                            'location_pick_up': location_pick_up})
