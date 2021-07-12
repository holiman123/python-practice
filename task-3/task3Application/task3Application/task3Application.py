import http.client
import json

def getCountriesList():
    connect = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "84ddb881f1mshe52cf4b1b8fbde2p1665f2jsnc71b246a3a81",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }

    connect.request("GET", "/api/npm-covid-data/", headers=headers)

    res = connect.getresponse()
    data = res.read()

    return list(json.loads(data.decode("utf-8")))

def getCountryStat(CountryIdentifyer):

    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "84ddb881f1mshe52cf4b1b8fbde2p1665f2jsnc71b246a3a81",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }

    conn.request("GET", "/api/covid-ovid-data/sixmonth/" + CountryIdentifyer, headers=headers)

    res = conn.getresponse()
    data = res.read()

    if data.decode("utf-8") == '[]':
        CountryList = getCountriesList()
        for i in range(len(CountryList)):
            if str(dict(CountryList[i]).get("TwoLetterSymbol")).lower() == CountryIdentifyer.lower() or str(dict(CountryList[i]).get("Country")).lower() == CountryIdentifyer.lower():
                return list(getCountryStat(dict(CountryList[i]).get("ThreeLetterSymbol")))
        return ""
    else:
        return list(json.loads(data.decode("utf-8")))

print(getCountryStat("ukraine")[0])