import json
from pathlib import Path
# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 1, "title": "True Liews", "year": 1995}
# ]
# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)

#read
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]) #dics!

