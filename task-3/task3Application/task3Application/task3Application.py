import http.client
import json

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "84ddb881f1mshe52cf4b1b8fbde2p1665f2jsnc71b246a3a81",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/covid-ovid-data/sixmonth/UKR", headers=headers)

res = conn.getresponse()
data = res.read()

parsedData = json.loads(data.decode("utf-8"))

print(parsedData)
