"""This module extract information from a csv file in the web and save it in the PC"""
from urllib import request

CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
DEST_PATH = r'C:\python_scripts\CSV_Files\Ripple.csv'

def download_csv_data(csv_url, dest_path):
    """This function request the file from the given url & save it into the file"""
    # open the url file
    response = request.urlopen(csv_url)
    # read the file
    csv = response.read()
    # convert into string
    csv_str = str(csv)
    # split lines into the file
    lines = csv_str.split("\\n")
    f_x = open(dest_path, "w")
    for line in lines:
        f_x.write(line + "\n")
    f_x.close()

download_csv_data(CSV_URL, DEST_PATH)
