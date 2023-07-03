import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432',
    database='hw_hillel_sql'
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM laptop;")

result = cursor.fetchall()
# print(result)

for laptop in result:
    print(laptop)

cursor.close()
connection.close()

