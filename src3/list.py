import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Following code added to replace environment variable.
# Note I could use local Jupyter, but this is portable, maybe.

db_url="postgres://sjxgnmkszhvvdc:d8add5033b1fec41278632fc2d7c50ddd0a28f07f066c9e3589cee6dbda7974c@ec2-174-129-33-181.compute-1.amazonaws.com:5432/d8oipsseui1nq1"
engine = create_engine(db_url)

# engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))      # CREATES DIFFERENT SESSIONS TO PREVENT OVERLAP

formatted_query = '''\
    SELECT origin,
           destination,
           duration
    FROM   flights'''

def main():
    flights = db.execute(formatted_query).fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()
