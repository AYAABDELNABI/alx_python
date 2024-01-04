import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

path = "mysql+mysqldb://{}:{}@localhost/{}".format(
    username, password, database)
database = create_engine(path)

Base.metadata.create_all(bind=database)

Session = sessionmaker(bind=database)
session = Session()

states = session.query(State).first()

if states:
    print("{}: {}".format(states.id, states.name))
else:
    print("Nothing")

session.close()