import urllib
import urllib3
import datetime
import requests

urllib3.disable_warnings()

#url downloads for all the zip files daily

urlMon = 'https://downloads.leginfo.legislature.ca.gov/pubinfo_Mon.zip'
urlTue = 'https://downloads.leginfo.legislature.ca.gov/pubinfo_Tue.zip'
urlWed = 'https://downloads.leginfo.legislature.ca.gov/pubinfo_Wed.zip'
urlThu = 'https://downloads.leginfo.legislature.ca.gov/pubinfo_Thu.zip'
urlFri = 'https://downloads.leginfo.legislature.ca.gov/pubinfo_Fri.zip'
urlSat = 'https://downloads.leginfo.legislature.ca.gov/pubinfo_Sat.zip'
urlSun = 'https://downloads.leginfo.legislature.ca.gov/pubinfo_Sun.zip'

#day of the week
day = datetime.datetime.today().weekday()


if day == 0: 
    pub = requests.get(urlSun, verify = False)
    with open('pubinfo_Sun.zip', 'wb') as f: 
        f.write(pub.content)

elif day == 1: 
    pub = requests.get(urlMon, verify = False)
    with open('pubinfo_Mon.zip', 'wb') as f:
        f.write(pub.content)

elif day == 2: 
    pub = requests.get(urlTue, verify = False)
    with open('pubinfo_Tue.zip', 'wb') as f:
        f.write(pub.content)

elif day == 3: 
    pub = requests.get(urlWed, verify = False)
    with open('pubinfo_Wed.zip', 'wb') as f:
        f.write(pub.content)

elif day == 4:
    pub = requests.get(urlThu, verify = False)
    with open('pubinfo_Thu.zip', 'wb') as f:
        f.write(pub.content)

elif day == 5: 
    pub = requests.get(urlFri, verify = False)
    with open('pubinfo_Fri.zip', 'wb') as f:
        f.write(pub.content)

else: 
    pub = requests.get(urlSat, verify = False)
    with open('pubinfo_Sat.zip', 'wb') as f:
        f.write(pub.content)


