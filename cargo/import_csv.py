import psycopg2

# connection establishment
conn = psycopg2.connect(
    database="cargo",
    user='postgres',
    password='password',
    host='localhost',
    port='5432'
)

conn.autocommit = True

# Creating a cursor object
cursor = conn.cursor()

# query to create a table
sql = ''' CREATE TABLE locations (city VARCHAR(50), state VARCHAR(50), zip INT, age INT, latitude INT,longtitude INT); '''

# executing above query
cursor.execute(sql)
print("Table has been created successfully!!")

# Closing the connection
conn.close()


# conn = psycopg2.connect(database="Nordwind Taders", user="postgres", password="12345",
#                         host="localhost")  # , port="5432"

# path = 'suppliers.json'
# cur = conn.cursor()
# cur.execute('select * from student')
# rows = cur.fetchall()

# conn.autocommit = True
# with open('suppliers.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     data_ = []
#     # print(type(data))
#     # data_sppl = csv.DictReader(f);
#     # index = 1
#     # supl_country_lst=[]
#     # # supl_country_lst.append
# # def str_lst():
# #
# # str_lst(lst)
#
#     for i in data:##Zapoliaem suppliers
#         # index = 0
#         # ii = ', '.join(i.get("products"))
#         # print(ii)
#
#         cur.execute(
#             'INSERT INTO suppliers(company_name, contact, address, phone, fax, homepage, products, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
#             (i.get('company_name'), i.get('contact'), i.get('address'), i.get('phone'), i.get('fax'), i.get("homepage"),
#              ', '.join(i.get("products")), i.get('address').split(';')[0]))


        # with open('uszips.csv', 'r', encoding='utf-8') as f1:  # Пока не решил, что делать, просто открыл
        #     with open('suppliers.csv', 'r', encoding='utf-8') as f2:  # Скачать наверное без заголовка надо
        #         data1 = csv.reader(f1, delimiter=',')  # products
        #         data2 = csv.reader(f2, delimiter=',')  # suppliers
        #         data_supl = []
        #         data_prod = []
        #         # prod = set()
        #         prod = []  # Spisok productov
        #         for ii in data1:
        #             data_prod.append(ii)
        #         for i in data2:
        #             data_supl.append(i)