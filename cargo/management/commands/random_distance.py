import os, csv
import random
from django.core.management import BaseCommand
from geopy.distance import geodesic

filename = "uszips.csv"


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(os.path.getsize(filename))
        # random row:

        with open(filename) as f:
            reader = csv.reader(f)
            chosen_row_pick_up = tuple(random.choice(list(reader)))
            print('Место отправления', chosen_row_pick_up[3], chosen_row_pick_up[-1])
            lat_pick_up = chosen_row_pick_up[1]
            lon_pick_up = chosen_row_pick_up[2]
            location1 = f"{lat_pick_up}, {lon_pick_up}"
        with open(filename) as f:
            reader = csv.reader(f)
            chosen_row_destination = random.choice(tuple(reader))
            print('Место прибытия', chosen_row_destination[3], chosen_row_destination[-1])
            lat_dest = chosen_row_destination[1]
            lon_dest = chosen_row_destination[2]
            location2 = f"{lat_dest}, {lon_dest}"

            from geopy.distance import distance
            dist = distance(location1, location2).miles
            print('Расстояние в милях ', dist)