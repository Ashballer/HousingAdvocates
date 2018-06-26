import zipfile
import urllib.request
import urllib.parse
import datetime

# where to download files 

url  = 'https://downloads.leginfo.legislature.ca.gov'

# extracting zip files from downloads folder into pubinfo 

day = datetime.datetime.today().weekday()

if day == 0:
    zip_ref = zipfile.ZipFile('C:/pubinfo/pubinfo_Sun.zip', 'r')
elif day == 1:
    zip_ref = zipfile.ZipFile('C:/pubinfo/pubinfo_Mon.zip', 'r')
elif day == 2:
    zip_ref = zipfile.ZipFile('C:/pubinfo/pubinfo_Tue.zip', 'r')
elif day == 3:
    zip_ref = zipfile.ZipFile('C:/pubinfo/pubinfo_Wed.zip', 'r')
elif day == 4:
    zip_ref = zipfile.ZipFile('C:/pubinfo/pubinfo_Thu.zip', 'r')
elif day == 5:
    zip_ref = zipfile.ZipFile('C:/pubinfo/pubinfo_Fri.zip', 'r')
elif day == 6:
    zip_ref = zipfile.ZipFile('C:/pubinfo/pubinfo_Sat.zip', 'r')

zip_ref.extractall('C:/pubinfo/dailyUpdate')
zip_ref.close()

