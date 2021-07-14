# Covid-19 statistical telegram bot

Telegram bot that shows statistical data about Covid.<br>

---



---

### How to use:

When program starts, it shows list, sorted by total cases of Covid, of countries information.<br>
To reload list press **"reset"** button.<br>
To see information about specific country write its name / ISO 3166-1 alpha-3 / ISO 3166-1 alpha-2, and press **"search"** button.

#### Elements review:

1) **Input text line**: input for country identifyer to find its information.
2) **Search button**:   button to start search procces.
3) **Reset button**:    button to reload all countries list.
4) **Info area**:       area to output info about countries.  

---

### Code review:
Source code has class of UI, some main methods and buttons event methods.

#### UI class:
Original created in Qt Designer, and edited by myself to add methods *(createLabels, ResetPressed, SearchPressed)*.<br>
There is also standart methods *(setupUI, retranslateUi)*.

#### Methods:
1) **"getCountriesList"**: get list of dictionaries of all countries information.<br>
2) **"getCountryStat"**: get list of dictionaries of countries information that match to input country identifyer.<br>
3) **"niceStringFormat"**: format string to nice look.<br>
4) **"createLabels"**: create list of labels that contains countries information.<br>
5) **"setupUi"**: set all UI widgets.<br>
6) **"retranslateUi"**: set static texts.<br>

#### Also there is two buttons event functions:
7) **"ResetPressed"**: reset button event.<br>
8) **"SearchPressed"**: search button event.<br>

---
#### Author: Daniil Luchitskyi KI-20010B.
