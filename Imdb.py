from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import socket
import os
from ping_cmd import host
import zipfile
import requests
from datetime import *
import time
import subprocess
import argparse
from bs4 import BeautifulSoup
import re
import requests
from collections import defaultdict
import datetime
import requests
import pandas as pd

elements_parser = argparse.ArgumentParser()
elements_parser.add_argument('page', metavar='page', type=str, help='The IMDB URL of the movie')

elements_parser.add_argument('path', metavar='path', type=str, help='Path of review write location')

elements_parser.add_argument('number_of_pages', metavar='number_of_pages', type=str, help='Number of pages to scrape')

args = elements_parser.parse_args()

page = args.page
write_loc = args.path
num_pages = args.number_of_pages

driver = webdriver.Chrome('./chromedriver')



def page_load(page, write_loc, num_pages):
    driver.get(page)

    #num_pages = 20

    i = 0

    while i < int(num_pages):
        try:
            driver.find_element_by_xpath('//*[(@id = "load-more-trigger")]').click()
            time.sleep(0.5)
            i += 1
        except Exception as e:
            print(e)


    soup = BeautifulSoup(driver.page_source, 'html.parser')
    reviews = [re.sub(r'(\n+)(?=[A-Z])', r'', str(x.text)) for x in soup.find_all(class_='text show-more__control')]
    ratings = [str(x.span.text) for x in soup.find_all(class_='rating-other-user-rating')]
    name = soup.find_all(class_='parent')[0].a.text
    review_ratings = defaultdict(dict)
    for x in range(len(reviews)):
        review_ratings[x]['rating'] = ratings[x]
        review_ratings[x]['review'] = reviews[x]

    df = pd.concat({k: pd.DataFrame.from_dict(v, 'index').T for k, v in review_ratings.items()}, axis=0)

    path = write_loc + '/'+name

    try:
        os.mkdir(path)
    except Exception as e:
        print(e)

    df.to_csv(path +'/review_extract_' + datetime.datetime.today().strftime('%Y-%m-%d') + '.csv', index=False)

    print('Scraping completed!')


page_load(page, write_loc, num_pages)

