import sqlite3
from pathlib import Path
import json

movies = json.loads(Path("movies.json").read_text())
# print(movies[0])
with sqlite3.connect("db.sqllite3") as conn:
    command = "INSERT INTO movies valies(?,?,?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()


# get https://sqlitebrowser.org/dl/  create table called movies
#read
# with sqlite3.connect("db.sqllite3") as conn:
#     command = "SELECT * from movies"
#     cursor = conn.execute(command)
#     for movie in cursor:
#         print(movie)

