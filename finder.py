'''
OVERVIEW OF THE FINDER APPLICATION

- program desgined to find variety of food, drinks, etc. in a given location
- uses selenium for the web scraping feature in order to utilize Google Maps to retrieve information
- sorts the results by a filter, leaning towards categorizing by reviews to start
    - the reviews will be stored in an array, holding the most five recent?
    - the information will be displayed if requested

- prompt the user if they want to search by zip code or city name

- may leverage an algorithm that finds keywords to display information about the places
- ex. In-N-Out: 4.5 Stars, reviewers commonly described this place as "cheap, convenient, tasty"
    
'''

from selenium import webdriver # imports the webdriver
from selenium.webdriver.common.keys import Keys # allows us to use input
from selenium.webdriver.common.by import By # 

# google maps url:  https://www.google.com/maps/@32.7678627,-117.0676283,3643m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MDMxOC4wIKXMDSoJLDEwMjExNjQwSAFQAw%3D%3D
url = 'https://www.google.com/maps/@32.7678627,-117.0676283,3643m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MDMxOC4wIKXMDSoJLDEwMjExNjQwSAFQAw%3D%3D'

driver = webdriver.Chrome() # browser to use
driver.get(url)
