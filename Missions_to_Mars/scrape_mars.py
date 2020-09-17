from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd

def scrape_all():

    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", executable_path="chromedriver", headless=False)

    collection = {
        "Title": title,
        "Paragraph": pgrph
        "Featured Image": featured_image_url
        "date": dt.datetime.now()
    }

    browser.quit()
    return collection
