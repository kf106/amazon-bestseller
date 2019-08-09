## Scrape all Amazon sites for your product's Amazon Bestseller Rankings

Selenium + Python application that takes your Amazin AIN product identifier as its first and only argument, visits each site in turn, scrapes the data and presents your cross-site rankings in the Selenium window at the end.

Install with `sudo ./install.sh`

Activate environment with `source venv/bin/activate`

Run with `python amazon-bestseller.py <AIN>`

This script requires ChromeDriver, which can be downloaded from https://chromedriver.chromium.org/downloads

Get the one that matches your current Chrome install and put it in `~/.local`

For example:

![Screenshot](docs/img/screenshot.png)
