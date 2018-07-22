import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():

    f = open("zipsver1.csv")
    reader = csv.reader(f)

    for i, row in enumerate(reader):

        if i == 0:
            continue

        db.execute("""INSERT INTO "tblZip" (zipcode, city, state, latitude, longitude, population) VALUES (:a, :b, :c, :d, :e, :f)""", {"a": row[0], "b": row[1], "c": row[2], "d": row[3], "e": row[4], "f": row[5]})

    db.commit()

if __name__ == "__main__":
    main()
