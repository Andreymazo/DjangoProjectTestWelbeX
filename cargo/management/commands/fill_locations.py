import asyncio
import os, csv
import shutil
import time

import aiofiles
import asyncpg
from aiocsv import AsyncReader
from django.core.management import BaseCommand

filename = "uszips.csv"


# https://magicstack.github.io/asyncpg/current/usage.html

# def copy_one():
#     import psycopg2
#
#     # connection establishment
#     conn = psycopg2.connect(
#         database="newdb",
#         user='postgres',
#         password='123456',
#         host='localhost',
#         port='5432'
#     )
# conn.autocommit = True

# Creating a cursor object
# cursor = conn.cursor()
# with open(filename, 'r', encoding='utf-8') as f:
#     data = csv.reader(f, delimiter=',')
#     next(data)
#
#     for i in data:  ##Zapoliaem suppliers
# cursor.execute(
#     'INSERT INTO cargo_locations( "zip", "latitude", "longtitude", "city", "state") VALUES (%s, %s, %s, %s, %s)',
#     (i[0], i[1], i[2], i[3], i[5].split(',')[0]))
# query to create a table
# sql = '''drop table locations'''
# sql = ''' CREATE TABLE cargo_locations (zip INT, latitude FLOAT, longtitude FLOAT, city VARCHAR(50), state VARCHAR(50)); '''
# sql = '''truncate table cargo_locations restart identity cascade'''
# sql = '''COPY cargo_locations FROM '/home/andrey_mazo/PycharmProjects/DjangoProjectCargoTest/cargo/templates/tmp/uszips.csv' WITH (FORMAT csv);'''
# sql = '''COPY cargo_locations FROM '/home/andrey_mazo/PycharmProjects/DjangoProjectCargoTest/cargo/templates/tmp/uszips.csv' DELIMITER ',' CSV HEADER;'''
# sql = \copy cargo_locations FROM '/path/to/csv/ZIP_CODES.txt' DELIMITER ',' CSV
# cursor.execute(sql)

async def fill_locations():
    filepath_1 = 'temp1'
    g = len(os.listdir(filepath_1))  # 68

    # for f in asyncio.as_completed([x(i) for i in range(10)]):
    #     result = await f
    # async def async_range(count):
    #     for i in range(count):
    #         yield (i)
    #         await asyncio.sleep(0.0)
    # class asyncrange:
    #
    #     class __asyncrange:
    #         def __init__(self, *args):
    #             self.__iter_range = iter(range(*args))
    #
    #         async def __anext__(self):
    #             try:
    #                 return next(self.__iter_range)
    #             except StopIteration as e:
    #                 raise StopAsyncIteration(str(e))
    #
    #     def __init__(self, *args):
    #         self.__args = args
    #
    #     def __aiter__(self):
    #         return self.__asyncrange(*self.__args)

    # async for j in asyncrange(1, g, 1):  # asyncio.as_completed(range(1, g)):

    async def async_generator():
        # normal loop
        for i in range(1, g+1):
            # block to simulate doing work
            await asyncio.sleep(1)
            # yield the result
            yield i

    # for j in range(1, g):
    async for j in async_generator():
        async with aiofiles.open(f'temp1/newfile_{j}.csv', 'r', encoding='utf-8') as f:
    # async with aiofiles.open('uszips.csv', 'r', encoding='utf-8') as f:

            async for i in AsyncReader(f):
            # data = csv.reader(f, delimiter=',')
            # next(data)
            # for i in data:
            #     import asyncpg
                import psycopg2
                conn = await asyncpg.connect(
                    database="newdb",
                    user='postgres',
                    password='123456',
                    host='localhost',
                    port='5432'
                )
                # https: // magicstack.github.io / asyncpg / current / usage.html
                await conn.execute('''INSERT INTO cargo_locations("zip", "latitude", "longtitude", "city", "state") \
                VALUES ($1, $2, $3, $4, $5)''', i[0], i[1], i[2], i[3], i[5])
                # conn.autocommit = True
                # cursor = conn.cursor()
                # #
                # cursor.execute(
                #     'INSERT INTO cargo_locations( "zip", "latitude", "longtitude", "city", "state") VALUES (%s, %s, %s, %s, %s)',
                #     (i[0], i[1], i[2], i[3], i[5].split(',')[0]))
                # conn.close()

                # '''COPY cargo_locations("zip", "latitude", "longtitude", "city", "state") from '/home/andrey_mazo/PycharmProjects/DjangoProjectCargoTest/temp1/newfile_1.csv' CSV HEADER;''')
                # '''/COPY cargo_locations FROM '/home/andrey_mazo/PycharmProjects/DjangoProjectCargoTest/uszips.csv' DELIMITER ',' CSV HEADER;'''
                # )
                # await conn.close
            time.sleep(0.5)
            print(f'___________{j}__________________')

        # task1 = asyncio.create_task(fill_locations())
        # await task1


class Command(BaseCommand):

    def handle(self, *args, **options):
        # filepath_1 = 'temp1'
        # g = len(os.listdir(filepath_1))  # 68
        # for j in range(1, g):
        #     with open(f'temp1/newfile_{j}.csv', 'r', encoding='utf-8') as f:
        #         data = csv.reader(f, delimiter=',')
        #         next(data)
        #         for i in data:
        #             # import psycopg2
        #             import psycopg2
        #             conn = psycopg2.connect(
        #                 database="newdb",
        #                 user='postgres',
        #                 password='123456',
        #                 host='localhost',
        #                 port='5432'
        #             )
        #
        #             conn.autocommit = True
        #             cursor = conn.cursor()
        #             #
        #             cursor.execute('INSERT INTO cargo_locations( "zip", "latitude", "longtitude", "city", "state") VALUES (%s, %s, %s, %s, %s)',
        #                 (i[0], i[1], i[2], i[3], i[5].split(',')[0]))
        #             conn.close()
        #
        #                 # '''COPY cargo_locations("zip", "latitude", "longtitude", "city", "state") from '/home/andrey_mazo/PycharmProjects/DjangoProjectCargoTest/temp1/newfile_1.csv' CSV HEADER;''')
        #             # '''/COPY cargo_locations FROM '/home/andrey_mazo/PycharmProjects/DjangoProjectCargoTest/uszips.csv' DELIMITER ',' CSV HEADER;'''
        #             # )
        #         time.sleep(1)
        #         print(f'___________{j}__________________')
        # fill_locations()
        # j = fill_locations()
        # asyncio.run(j)
        # loop=asyncio.get_event_loop()
        # loop.run_until_complete(fill_locations())
        asyncio.get_event_loop().run_until_complete(fill_locations())
