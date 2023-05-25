import os, csv
import shutil
import time

from django.core.management import BaseCommand

filename = "uszips.csv"


def copy_one():
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
    # with open(filename, 'r', encoding='utf-8') as f:
    #     data = csv.reader(f, delimiter=',')
    #     next(data)
    #
    #     for i in data:  ##Zapoliaem suppliers
    cursor.execute(
        'INSERT INTO cargo_locations( "zip", "latitude", "longtitude", "city", "state") VALUES (%s, %s, %s, %s, %s)',
        (i[0], i[1], i[2], i[3], i[5].split(',')[0]))
    # query to create a table
    # sql = '''drop table locations'''
    # sql = ''' CREATE TABLE cargo_locations (zip INT, latitude FLOAT, longtitude FLOAT, city VARCHAR(50), state VARCHAR(50)); '''
    # sql = '''truncate table cargo_locations restart identity cascade'''
    # sql = '''COPY cargo_locations FROM '/home/andrey_mazo/PycharmProjects/DjangoProjectCargoTest/cargo/templates/tmp/uszips.csv' WITH (FORMAT csv);'''
    # sql = '''COPY cargo_locations FROM '/home/andrey_mazo/PycharmProjects/DjangoProjectCargoTest/cargo/templates/tmp/uszips.csv' DELIMITER ',' CSV HEADER;'''
    # sql = \copy cargo_locations FROM '/path/to/csv/ZIP_CODES.txt' DELIMITER ',' CSV
    # cursor.execute(sql)


class Command(BaseCommand):

    def handle(self, *args, **options):
        filepath_1 = 'temp1'
        g = len(os.listdir(filepath_1))  # 68
        for j in range(1, g):
            with open(f'temp1/newfile_{j}.csv', 'r', encoding='utf-8') as f:
                data = csv.reader(f, delimiter=',')
                next(data)
                for i in data:
                    # import psycopg2
                    import psycopg2
                    conn = psycopg2.connect(
                        database="newdb",
                        user='postgres',
                        password='123456',
                        host='localhost',
                        port='5432'
                    )

                    conn.autocommit = True
                    cursor = conn.cursor()
                    #
                    cursor.execute('INSERT INTO cargo_locations( "zip", "latitude", "longtitude", "city", "state") VALUES (%s, %s, %s, %s, %s)',
                        (i[0], i[1], i[2], i[3], i[5].split(',')[0]))
                    conn.close()

                        # '''COPY cargo_locations("zip", "latitude", "longtitude", "city", "state") from '/home/andrey_mazo/PycharmProjects/DjangoProjectCargoTest/temp1/newfile_1.csv' CSV HEADER;''')
                    # '''/COPY cargo_locations FROM '/home/andrey_mazo/PycharmProjects/DjangoProjectCargoTest/uszips.csv' DELIMITER ',' CSV HEADER;'''
                    # )
                time.sleep(1)
                print(f'___________{j}__________________')


