"""
This a module for Object Relational Mapping project
which start with task 0  that has select statment
"""
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name_searched = sys.argv[4]

connection = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database)

cursor = connection.cursor()

# To pass SQL injection defined variable of type dictionary
# that holds the value of state needed and refer to it using key

state_name = {"state": state_name_searched}

query = "SELECT * FROM states \
            WHERE name COLLATE utf8mb4_bin = %(state)s"

cursor.execute(query, state_name)

States = cursor.fetchall()

for state in States:
    print(state)