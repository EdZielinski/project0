import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    #locations = db.execute("SELECT zipcode, city, state, latitude, longitude, population FROM tblZip").fetchall()
    locations = db.execute("SELECT zipcode FROM tblZip").fetchall()
    #for location in locations:
        # print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")
        #print(location)

if __name__ == "__main__":
    main()
