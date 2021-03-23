#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# URL of page to be scraped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

# open the url
browser.visit(url)

# scrape the url
html = browser.html
soup = BeautifulSoup(html, 'lxml')

# narrow it down to latest news story
result = soup.find('div', class_='list_text')

# extract headline and paragraph
news_title = result.find("a").text
news_p = result.find("div", class_="article_teaser_body").text

# Declare JPL url as variable
jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

# open jpl_url in browser
browser.visit(jpl_url)

#create html object
jpl_html = browser.html

# parse html with beautifulsoup
jpl_soup = BeautifulSoup(jpl_html, 'lxml')

# narrow down the results and find the image url
header = jpl_soup.find('div', class_="floating_text_area")
img = header.find("a")['href']
img_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/" + str(img)

# scrape Mars facts
facts_url = 'https://space-facts.com/mars/'

#convert table to pandas
tables = pd.read_html(facts_url)

# filter out Mars-Earth comparison
df = tables[0]

# convert table to html
html_table = df.to_html(header=False, index=False)
html_table.replace('\n', '')

# scrape hemisphere images
hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemi_url)

#create html object
hemi_html = browser.html

# parse html with beautifulsoup
hemi_soup = BeautifulSoup(hemi_html, 'lxml')

#create html object
hemi_html = browser.html

# parse html with beautifulsoup
hemi_soup = BeautifulSoup(hemi_html, 'lxml')
descriptions = hemi_soup.find("div", class_="description")

# create lists
mars_hemispheres = []
hemispheres = ['Cerberus', 'Schiaparelli', 'Syrtis Major','Valles Marineris']

# loop through each picture and pull out the img link and title
for hemisphere in hemispheres:
    
    # loop within the soup all the hemispheres ['Cerberus', 'Schiaparelli', 'Syrtis Major','Valles Marineris']
    try:
        #Click on image
        browser.click_link_by_partial_text(hemisphere)
        #create html object
        hemi_html = browser.html
        # parse html with beautifulsoup
        hemi_soup = BeautifulSoup(hemi_html, 'lxml')
        # narrow it down to the div class = downloads
        downloads = hemi_soup.find("div", class_="downloads")
        #find img url
        mars_img = downloads.find("a")["href"]
        #append mars_img to hemi_imgs list
        title = hemi_soup.find("h2", class_="title").text
        #split content to take out the word enhanced
        title = str(title.split(" ")[0])+" "+str(title.split(" ")[1])

        # store values in a dictionary
        mars_dict = {
            "title":title,
            "image_url":mars_img
        }
        mars_hemispheres.append(mars_dict)
        
        
        # go back to landing page
        browser.visit(hemi_url)

    except AttributeError as e:
        print(e)

