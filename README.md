# web-scraping-challenge
This repository contains the code needed to scrape current information about NASA's Mars mission and put that information on a dynamic html dashboard.


mission_to_mars.ipynb - This is a Jupyter Notebook file that contains the code to scrape the data from four different websites using Splinter and BeautifulSoup. 


    First, it collects the lates news headline and paragraph text from NASA's Mars News Site and stores the variable for later reference.


    Next, the code scapes the image url for the current featured image from the Jet Propulsion Lab's Mars Space Images page.


    Then, the code scrapes a table of Mars facts and converts it to an HTML table.


    Finally, the code uses a for loop to scrape an image url of each of Mars's hemispheres and the name of the hemisphere which is stored in a list of dictionaries.


scrape_mars.py - This is file takes the Jupyter Notebook code and:


    converts it to a Python script
    
    creates a function called scrape that executes all of the scraping code from the notebook
    
    returns it to one Python dictionary containing all of the scraped data


app.py:


    Creates a route called "/scrape" that  imports the scrape_mars.py script and calls the scrape function.

    Stores the return value in Mongo as a Python dictionary.

    Creates a root route "/" that queries the Mongo database and passes the mars data into an HTML template to display the data.
    
 
 index.html - This html page is located in the "templates" folder.
 
    The html page displays all of the scraped data on an online dashboard
    
    The "Scrape New Data" button calls the scrape function and updates the dashboard with the latest info
