"""
This a module for Object Relational Mapping project
which start with task 0  that has select statment
"""
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]


connection = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database)

cursor = connection.cursor()

state = {"name": state_name}
query = "SELECT name FROM cities WHERE state_id in\
        (SELECT id FROM states WHERE name = %(name)s)"

cursor.execute(query, state)

Cities = cursor.fetchall()
# Using list of comperhension to hold city names
city_name = [city[0] for city in Cities]
print(", ".join(city_name))