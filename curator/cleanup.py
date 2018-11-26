import requests
from requests.auth import HTTPBasicAuth
import datetime
import dateutil.parser
import time
import os
import sys
import logging

username = os.getenv("ES_USERNAME")
password = os.getenv("ES_PASSWORD")
url = os.getenv("ES_URL")
search_prefix = os.getenv("ES_PREFIX", "3scale")
if not username or not password or not url:
    logging.info("Please define ES_USERNAME ES_PASSWORD ES_URL env vars")
    sys.exit()
number_of_days = int(os.getenv("NUMBER_OF_DAYS", 7))
cutoff_date =  datetime.datetime.now() - datetime.timedelta(days=number_of_days)
indices_to_delete = []

while True:
    try:
        response = requests.get(
            url=url+"/_cat/indices?h=i,creation.date.string&format=json",
            auth=HTTPBasicAuth(username, password),
            verify=False
        )
        print("Cutoff date is " + str(cutoff_date))
        for index in response.json():
            print("Index date is " + index["creation.date.string"])
            if cutoff_date >= dateutil.parser.parse(
                index["creation.date.string"]
            ).replace(tzinfo=None) and search_prefix in index['i']:
                indices_to_delete.append(index['i'])

        if not indices_to_delete:
            logging.info("No indices to delete")
        for index in indices_to_delete:
            response = requests.delete(
                url=url+"/"+index,
                auth=HTTPBasicAuth(username, password),
                verify=False
            )
            logging.info(response.content)
        time.sleep(60*60)
    except Exception as e:
        logging.error(e)
