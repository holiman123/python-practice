import telebot
import config
import http.client
import json

from telebot import types

# get list of dictionaries of all countries information
def getCountriesList():
    connect = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "84ddb881f1mshe52cf4b1b8fbde2p1665f2jsnc71b246a3a81",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }

    connect.request("GET", "/api/npm-covid-data/", headers=headers)

    res = connect.getresponse()
    data = res.read()

    resList = list(json.loads(data.decode("utf-8")))
    del resList[0:2]

    return resList

# get list of dictionaries of countries information that match to input country identifyer
def getCountryStat(CountryIdentifyer):

    CountriesList = getCountriesList()
    resList = []

    for i in CountriesList:
        if str(dict(i).get("Country")).lower().startswith(CountryIdentifyer.lower()):
            resList.append(dict(i))
        if str(dict(i).get("ThreeLetterSymbol")).lower() == CountryIdentifyer.lower():
            resList.append(dict(i))
        if str(dict(i).get("TwoLetterSymbol")).lower() == CountryIdentifyer.lower():
            resList.append(dict(i))

    return resList

# format string to nice look
def niceStringFormat(inputString):

    resString = inputString.split("/")
    for i in range(5 - len(resString[0])):
        resString[0] += (" ")
    for i in range(25 - len(resString[1])):
        resString[1] += (" ")
    for i in range(25 - len(resString[2])):
        resString[2] += (" ")
    for i in range(25 - len(resString[3])):
        resString[3] += (" ")
    for i in range(20 - len(resString[4])):
        resString[4] += (" ")
    return str(' '.join(resString))

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("See countries list by total cases rate")

    markup.add(button1)

    bot.send_message(message.chat.id, "Welcome to Covid-19 statistical bot!\nSee countries list or write country name/two letter symbol/three letter symbol", reply_markup=markup)


def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='get file', callback_data="temp"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    open("Covid countries statistics.txt", "w", encoding="utf-8").write("")
    file = open("Covid countries statistics.txt", "a", encoding="utf-8")    
    tempCountriesList = getCountriesList()
    for i in range(len(tempCountriesList)):
        file.write(str(niceStringFormat(" " + str(i + 1) + ")/" + dict(tempCountriesList[i]).get("Country") + "/Total cases: " + str(dict(tempCountriesList[i]).get("TotalCases")) + "/Infection risk: " + str(dict(tempCountriesList[i]).get("Infection_Risk")) + "/Total death: " + str(dict(tempCountriesList[i]).get("TotalDeaths")) + "/Total recovered: " + str(dict(tempCountriesList[i]).get("TotalRecovered"))) + "\n"))
    bot.send_document(call.message.chat.id, open("Covid countries statistics.txt"))

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    if message.text == "See countries list by total cases rate":
        tempCountriesList = getCountriesList()
        for i in range(4):
            bot.send_message(message.chat.id, " " + str(i + 1) + ") " + dict(tempCountriesList[i]).get("Country") + "\nTotal cases: " + str(dict(tempCountriesList[i]).get("TotalCases")) + "\nInfection risk: " + str(dict(tempCountriesList[i]).get("Infection_Risk")) + "\nTotal death: " + str(dict(tempCountriesList[i]).get("TotalDeaths")) + "\nTotal recovered: " + str(dict(tempCountriesList[i]).get("TotalRecovered")))
        bot.send_message(message.chat.id, " " + str(5) + ") " + dict(tempCountriesList[4]).get("Country") + "\nTotal cases: " + str(dict(tempCountriesList[4]).get("TotalCases")) + "\nInfection risk: " + str(dict(tempCountriesList[4]).get("Infection_Risk")) + "\nTotal death: " + str(dict(tempCountriesList[4]).get("TotalDeaths")) + "\nTotal recovered: " + str(dict(tempCountriesList[4]).get("TotalRecovered")), reply_markup=gen_markup())
        
    else:
        tempCountry = dict(getCountryStat(message.text)[0])
        bot.send_message(message.chat.id, str(dict(tempCountry).get("rank")) + ") " + dict(tempCountry).get("Country") + "\nTotal cases: " + str(dict(tempCountry).get("TotalCases")) + "\nInfection risk: " + str(dict(tempCountry).get("Infection_Risk")) + "\nTotal death: " + str(dict(tempCountry).get("TotalDeaths")) + "\nTotal recovered: " + str(dict(tempCountry).get("TotalRecovered")))
bot.polling(none_stop=True)