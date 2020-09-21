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
    # featured_image_url = 'https://pyxis.nymag.com/v1/imgs/115/983/a29c15a3a8d80f5a81d9c80799b74157d1-01-rbg.rhorizontal.w700.jpg'
    return featured_image_url

# mars facts scrape
def MarsFacts():
    mars_facts_url='https://space-facts.com/mars/'
    mars_data = pd.DataFrame(pd.read_html(mars_facts_url)[0])
    table = mars_data.to_html(classes='data table', header = False, index = False)
    return table

#mars Hemispheres
def scrape_hemis():
    # browser = Browser("chrome", executable_path="../chromedriver")
    # browser.vist(url)
    # soup=BeautifulSoup(browser.html, 'htlm.parser')
    # results = soup.find(class_='collapsable').find_all('item')
    # for each_result in results:
    #     hemis = {}
    #     hemis['url'] = each_reslut.find('a')['href']
    #     results_list.append(hemis)
        results_list = ['one', 'two', 'three']
        return results_list

# main scrape function
def scrape_all():

    # executable_path = {"executable_path": "../chromedriver"}
    # browser = Browser("chrome", executable_path="../chromedriver", headless=False)
    # title, pgrph = mars_news(browser)
    # img_url = featured_image(browser)
    # mars_weather = twitter_weather(browser)
    # facts = mars_facts()
    # hemisphere_image_urls = hemisphere(browser)

    collection = {}
    collection["title"]= mars_news()[0]
    collection["pgrph"]= mars_news()[1]
    collection["img_url"]= featured_image_url()
    collection["table"]= MarsFacts()
    collection["date"]= dt.datetime.now()

    # browser.quit()
    return collection
