from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import datetime as dt
import time

executable_path = {'executable_path': '../chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
#NASA news Scrape
def mars_news():
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
    html=browser.html
    NewsSoup = BeautifulSoup(html, 'html.parser')
    results = NewsSoup.find('div', class_="list_text")
    Title = results.find('a').text
    Pgrph = NewsSoup.find('div', class_="article_teaser_body").text
    return Title, Pgrph

# NASA JPL Site Scraper
def featured_image_url():
    # open website and click full_image button
    JPL_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(JPL_url)
    image = browser.find_by_id('full_image')
    image.click()
    time.sleep(.5)
    more_info_element = browser.find_link_by_partial_text("more info")
    more_info_element.click()
    time.sleep(.5)
    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")
    image_url = image_soup.select_one("figure.lede a img").get("src")
    featured_image_url = (f'https://www.jpl.nasa.gov{image_url}')
    return featured_image_url

# mars facts scrape
def MarsFacts():
    mars_facts_url='https://space-facts.com/mars/'
    mars_data = pd.DataFrame(pd.read_html(mars_facts_url)[0])
    table = mars_data.to_html(classes='data table', header = False, index = False)
    return table

#mars Hemispheres
def scrape_hemis():
    browser = Browser("chrome", executable_path="../chromedriver")
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    results_list = []
    image_urls = []
    browser.visit(hemi_url)
    hemiSoup = BeautifulSoup(browser.html, 'html.parser')
    results = hemiSoup.find(class_='collapsible').find_all(class_='item')
    time.sleep(.5)
    for result in results:
        image_title=result.find(class_='description').find('a').find('h3').text
        results_list.append(image_title)
    for title in results_list:
        time.sleep(.5)
        browser.find_link_by_partial_text(title).click()
        imgSoup=BeautifulSoup(browser.html, 'html.parser')
        link=imgSoup.find(class_='downloads').find('ul').find('li').find('a')['href']
        image_urls.append(link)
        browser.back()
    return image_urls

# main scrape function
def scrape_all():

    collection = {}
    collection["title"]= mars_news()[0]
    collection["pgrph"]= mars_news()[1]
    collection["img_url"]= featured_image_url()
    collection["table"]= MarsFacts()
    collection["date"]= dt.datetime.now()
    collection["image_urls"]= scrape_hemis()

    # browser.quit()
    return collection
