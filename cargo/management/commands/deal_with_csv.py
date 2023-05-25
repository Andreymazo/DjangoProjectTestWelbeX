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
            print(chosen_row_pick_up)
            lat_pick_up = chosen_row_pick_up[1]
            lon_pick_up = chosen_row_pick_up[2]
            location1 = f"{lat_pick_up}, {lon_pick_up}"
        with open(filename) as f:
            reader = csv.reader(f)
            chosen_row_destination = random.choice(tuple(reader))
            lat_dest = chosen_row_destination[1]
            lon_dest = chosen_row_destination[2]
            location2 = f"{lat_dest}, {lon_dest}"

            from geopy.distance import distance
            dist = distance(location1, location2).miles
            print(dist)
        # https: // pypi.org / project / geopy /



            # ['24551', '37.36655', '-79.3268', 'Forest', 'VA', 'Virginia', 'TRUE', '', '26376', '137.3', '51019',
            #  'Bedford', '{"51019": 97.23, "51031": 2.42, "51680": 0.35}', 'Bedford|Campbell|Lynchburg',
            #  '51019|51031|51680', 'FALSE', 'FALSE', 'America/New_York']

            # "zip", "lat", "lng", "city", "state_id", "state_name", "zcta", "parent_zcta", "population", "density", "county_fips", "county_name", "county_weights", "county_names_all", "county_fips_all", "imprecise", "military", "timezone"

            # lat_dest = chosen_row[1]
            # lon_dest = chosen_row[2]
            # tup_destination = (lat_des, lon_des)
            # dist =
        import psycopg2

        # connection establishment
        conn = psycopg2.connect(
            database="newdb",
            user='postgres',
            password='123456',
            host='localhost',
            port='5432'
        )

        conn.autocommit = True

        # Creating a cursor object
        cursor = conn.cursor()

        # query to create a table
        # sql = '''drop table locations'''
        # sql = ''' CREATE TABLE locations (zip INT, latitude FLOAT, longtitude FLOAT, city VARCHAR(50), state VARCHAR(50)); '''
        # sql = '''truncate table locations restart identity cascade'''

        # cursor.execute(sql)
        with open(filename, 'r', encoding='utf-8') as f:
            data = csv.reader(f, delimiter=',')
            next(data)

            for i in data:  ##Zapoliaem suppliers

                # index = 0
                # ii = ', '.join(i.get("products"))
                # print(ii)

                cursor.execute(
                    'INSERT INTO locations( "zip", "latitude", "longtitude", "city", "state") VALUES (%s, %s, %s, %s, %s)',
                    (i[0], i[1], i[2], i[3], i[5].split(',')[0]))

        # sql = '''insert into table locations '''
        # executing above query

        print("Table has been created successfully!!")

        # Closing the connection
        conn.close()