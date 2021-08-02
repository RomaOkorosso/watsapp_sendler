import time
import pywhatkit
import datetime
import csv
import requests

MSG_TEXT = "TEST"


def check_connection():
    url = "https://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False


phone_numbers = []
file_name = input("Please write .csv file name")
if ".csv" not in file_name:
    file_name = file_name + ".csv"
with open(file_name) as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        phone_numbers.append(*row)

for item in phone_numbers:
    try:
        print(f"{datetime.datetime.now()} start send msg to {item}")
        time.sleep(0.5)
        if check_connection():
            pywhatkit.sendwhatmsg_instantly(item, MSG_TEXT,
                                            10,
                                            True)
            print(f"{datetime.datetime.now()} finish send msg to {item}")
        else:
            print(f"NO INTERNET")
            quit()
    except Exception as err:
        print(err)
        quit()
