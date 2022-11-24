#! python
import pymssql
from dotenv import load_dotenv
load_dotenv()

'''.env file
PYMSSQL_TEST_SERVER = "172.16.1.5"
PYMSSQL_TEST_USERNAME = "sa"
PYMSSQL_TEST_PASSWORD = "pwd1234"
'''

from os import getenv
server = getenv("PYMSSQL_TEST_SERVER")
user = getenv("PYMSSQL_TEST_USERNAME")
password = getenv("PYMSSQL_TEST_PASSWORD")

# import os
# server = os.getenv("PYMSSQL_TEST_SERVER")
# user = os.getenv("PYMSSQL_TEST_USERNAME")
# password = os.getenv("PYMSSQL_TEST_PASSWORD")

# server  = "172.16.1.5"
# user = "sa"
# password = "pwd1234"

conn = pymssql.connect(server, user, password, "testdb")
# cursor = conn.cursor()

cursor = conn.cursor(as_dict=True)

# cursor.execute("""IF OBJECT_ID('persons', 'U') IS NOT NULL
#     DROP TABLE persons
# CREATE TABLE persons (
#     id INT NOT NULL,
#     name VARCHAR(100),
#     salesrep VARCHAR(100),
#     PRIMARY KEY(id)
# )""")


# cursor.executemany(
#     "INSERT INTO persons VALUES (%d, %s, %s)",
#     [(1, 'John Smith', 'John Doe'), (2, 'Jane Doe', 'Joe Dog'), (3, 'Mike T.', 'Sarah H.')])
# # you must call commit() to persist your data if you don't set autocommit to True
# conn.commit()

# cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
# row = cursor.fetchone()
# while row:
#     print("ID=%d, Name=%s" % (row[0], row[1]))
#     row = cursor.fetchone()




cursor.execute('SELECT * FROM persons;')
for row in cursor:
    print("ID=%d, Name=%s" % (row['id'], row['name']))


conn.close()
