from selenium import webdriver
import sys
import os
import json
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

home = os.getenv("HOME")

driver = webdriver.Chrome(home + '/.local/bin/chromedriver')
sites = ['com', 'co.uk', 'de', 'fr', 'es', 'com.mx', 'ca', 'co.jp', 'com.br', 'com.au', 'in' ]

html="<html><head></head><body><h1>" + sys.argv[1] + "</h1>"
failure = ""
success = True
first = True

for locale in sites:
    driver.get('https://www.amazon.' + locale + '/dp/' + sys.argv[1])
    if first:
        first = False
        html = html + "<p><b>" + driver.title + "</b></p>"
    try:
        rank_element = driver.find_element_by_css_selector('li[id="SalesRank"]')
        rank = rank_element.get_attribute('innerHTML')
        html = html + "<h2>" + locale + "</h2>"
        html = html + rank
    except:
        rank = "<p>No rank found</p>"
        success = False
        failure = failure + "<li>" + locale + "</li>"

if not success:
    html = html + "<h2> No results for:</h2><ul>" + failure + "</ul>"

html = html + "</body></html>"
file = open("result.html","w")
file.write(html)
file.close
html_file = Path.cwd() / "result.html"
driver.get(html_file.as_uri())
