import sqlite3
from pathlib import Path
import json

movies = json.loads(Path("movies.json").read_text())
# print(movies[0])
with sqlite3.connect("db.sqlite3") as conn:
    command = "create table movies (id int, title text, year int)"
    conn.execute(command)
    command = "INSERT INTO movies values(?,?,?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()
# get https://sqliteonline.com/
# read
    command = "SELECT * from movies"
    cursor = conn.execute(command)
    for movie in cursor:
        print(movie)
