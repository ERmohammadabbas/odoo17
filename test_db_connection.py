

import os
import psycopg2
from psycopg2 import OperationalError


db_name = os.getenv('postgres')
db_user = os.getenv('stu_id')
db_password = os.getenv('html')
db_host = os.getenv('127.0.0.1')
db_port = os.getenv('5438')

try:
    conn = psycopg2.connect(

        dbname ="postgres",
        user ='stu_id',
        # user='sham',
        password ="html",
        # password="sham1234",
        host ='127.0.0.1',  # Change 'test' to 'localhost'
        port = 5438
    )
    print("Connection successful")
except OperationalError as e:
    print(f"The error '{e}' occurred")