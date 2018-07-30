"""This module pretends to extract source html from web using 'requests' library"""
import requests

TEST = requests.get("http://www.hipstercode.com")
TEST2 = requests.get("https://www.google.com/")
DEST_PATH = r'C:\python_scripts\CSV_Files\Requests.txt'

#Returns all the html source code of the page
#print(str(TEST.text.encode('utf-8')))
NEW_FILE = open(DEST_PATH, "w")
TEST.encoding = 'ISO-8859-1'
NEW_FILE.write(str(TEST.text))
NEW_FILE.close()

#Get headers
print(TEST.headers)

#Get cookies
print(TEST.cookies.get_dict())
