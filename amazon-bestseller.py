from selenium import webdriver
import sys
import os
import json
import time
from pathlib import Path


if len(sys.argv) < 2:
    print("Product ASIN required as argument")
    sys.exit()

home = os.getenv("HOME")

driver = webdriver.Chrome(home + '/.local/bin/chromedriver')
# sites = ['com', 'co.uk', 'de', 'fr', 'es', 'com.mx', 'ca', 'co.jp', 'com.br', 'com.au', 'in' ]
sites = {
  "com": "Best Sellers Rank:",
  "co.uk": "Best Sellers Rank:",
  "de": "Amazon Bestseller-Rang:",
  "fr": "Classement des meilleures ventes ",
  "es": "Clasificación en los más vendidos de Amazon:",
  "com.mx": "Clasificación en los más vendidos de Amazon:",
  "ca": "Best Sellers Rank:",
  "co.jp": "Amazon Bestseller:",
  "com.br": "Ranking dos mais vendidos:",
  "com.au": "Best Sellers Rank:",
  "in": "Best Sellers Rank:"
}

html="<html><head></head><body><h1>" + sys.argv[1] + "</h1>"
failure = ""
success = True
first = True

for locale in sites:
    driver.get('https://www.amazon.' + locale + '/dp/' + sys.argv[1])
    time.sleep(1)
    search_string = sites.get(locale)
    if first:
        first = False
        html = html + "<p><b>" + driver.title + "</b></p>"
    try:
        print(sites.get(locale))
        rank_child = driver.find_elements_by_xpath("//*[contains(text(), '" + search_string + "')]")
        rank_element = rank_child[0].find_element_by_xpath('./../..')
        rank = rank_element.get_attribute('innerHTML')
        html = html + "<h2>" + locale + "</h2>"
        html = html + rank + "\n"
    except Exception as err:
        print(err)
        rank = "<p>No rank found</p>"
        success = False
        failure = failure + "<li>" + locale + "</li>"
    
if not success:
    html = html + "<h2> No results for:</h2><ul>" + failure + "</ul>"

html = html + "</body></html>"
file = open("result.html","w")
file.write(html)
file.flush()
file.close
time.sleep(1)
html_file = Path.cwd() / "result.html"
driver.get(html_file.as_uri())
