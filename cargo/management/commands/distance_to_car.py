from django.core.management import BaseCommand


def distance_to_point(lp1, lop1, lp2, lop2):
    lat_point1 = lp1
    lon_point1 = lop1
    location1 = f"{lat_point1}, {lon_point1}"
    lat_point2 = lp2
    lon_point2 = lop2
    location2 = f"{lat_point2}, {lon_point2}"
    from geopy.distance import distance
    dist = distance(location1, location2).miles
    print('Расстояние в милях ', dist)


class Command(BaseCommand):

    def handle(self, *args, **options):

        z, zz, zzz, zzzz = [float(s) for s in input().split(' ')]
        distance_to_point(z, zz, zzz, zzzz)
