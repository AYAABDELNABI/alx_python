"""
This a module for Object Relational Mapping project
which start with task 0  that has select statment
"""
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]


connection = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database)

cursor = connection.cursor()

query = "SELECT A.id, A.name, B.name FROM cities A,states B\
        WHERE A.state_id = B.id"

cursor.execute(query)

Cities = cursor.fetchall()

for city in Cities:
    print(city)