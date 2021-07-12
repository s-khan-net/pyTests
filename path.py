from pathlib import Path
from time import ctime
from zipfile import ZipFile

path = Path("test.txt")
path.write_text("data")
print(path.read_text())

print(ctime(path.stat().st_mtime))

for path in Path().rglob('*.*'):  # get all files in a path
    print(path)

#zip file
with ZipFile("zipfile.zip", 'w') as zip:
    for path in Path().rglob('*.*'):  # zip all files in the current path
        zip.write(path)

with ZipFile("zipfile.zip") as zip:
    print(zip.namelist())

#csv
import csv

with open("data.csv",'w') as file:
    writer = csv.writer(file)
    writer.writerow(["id","price"])
    writer.writerow([1,3])
    writer.writerow([2,33])
    writer.writerow(["3","price"])

with open("data.csv") as file:
    reader = csv.reader(file)
    #print(list(reader)) iterator reader has functionality to move next
    for row in reader:
        print(row)

