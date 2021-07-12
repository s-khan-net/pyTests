import requests

response = requests.get("https://masjidnear.me/api/Salaah/GetTimesList/lat/12.3490095/lng/76.6529183/method/1/day/1/month/2/year/2021/school/2/days/19")
times = response.json()["timesList"]
timeslist = [time for time in times]
print(times)