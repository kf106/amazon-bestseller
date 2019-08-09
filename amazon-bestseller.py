from selenium import webdriver
import sys
import os
import json
from selenium.webdriver.common.keys import Keys
import time

home = os.getenv("HOME")

driver = webdriver.Chrome(home + '/.local/bin/chromedriver')
sites = ['com', 'co.uk', 'de', 'fr', 'es', 'com.mx', 'ca', 'co.jp', 'com.br', 'com.au', 'in' ]

html="<html><head></head><body><h1>" + sys.argv[1] + "</h1>"

for locale in sites:
    driver.get('https://www.amazon.' + locale + '/dp/' + sys.argv[1])
    try:
        rank_element = driver.find_element_by_css_selector('li[id="SalesRank"]')
        rank = rank_element.get_attribute('innerHTML')
    except:
        rank = "<p>No rank found</p>"
    html = html + "<h2>" + locale + "</h2>"
    html = html + rank


html = html + "</body></html>"
driver.execute_script("document.write('{}')".format(json.dumps(html)))
