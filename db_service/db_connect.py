import psycopg2

dbname = 'postgres'
user = 'postgres'
password = 'docker'
host = 'localhost'
port = '5432'
sql_statement = '''CREATE TABLE USERS
(
    Id SERIAL PRIMARY KEY,
    Email TEXT
    FirstName TEXT
    LastName TEXT
);'''
conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
print("Connect: ")
print(conn)
cursor = conn.cursor()
cursor.execute(sql_statement)
conn.commit()
