'''
OVERVIEW OF THE FINDER APPLICATION

- program desgined to find variety of food, drinks, etc. in a given location
- uses selenium for the web scraping feature in order to utilize Google Maps to retrieve information
- sorts the results by a filter, leaning towards categorizing by reviews to start
    - the reviews will be stored in an array, holding the most five recent?
    - the information will be displayed if requested

- greet the user
- prompt the user if they want to search by zip code or city name
    - if statements to control proper input
    - loop until the correct response has been found
- query the input
    - ensure that the input is valid?

- may leverage an algorithm that finds keywords to display information about the places
- ex. In-N-Out: 4.5 Stars, reviewers commonly described this place as "cheap, convenient, tasty"
    
'''
import location

from selenium import webdriver # imports the webdriver
from selenium.webdriver.common.keys import Keys # allows us to use input
from selenium.webdriver.common.by import By 

import time

url = 'https://www.google.com/maps'

query = input('What are you searching for: ')

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options = options)
driver.get(url)

driver.implicitly_wait(5) # using an implicit wait to help us sync browser and code so that it does not return an exception

'''
# implement code to find the text box
# enter the infomraiton
# search
# creating a variable for the search box
'''

searchBox = driver.find_element(By.ID, 'searchboxinput')
searchBox.clear()
searchBox.send_keys(f'{query}')
searchBox.send_keys(Keys.ENTER)

# holds the list of locations that appear on query finish

# xpath for price and address: //div/span[3]/span[2]

def scrollAndCollect(scrolls):
    results_panel = driver.find_element(By.XPATH, "//div[@role='feed']")
    
    # avoid duplicates
    seenLocations = set()
    allLocations = []
    
    # scroll many times to load
    for i in range(scrolls):
        # scrolling
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", results_panel)
        time.sleep(2) # wait
        
        # all location currently visible
        locationNames = driver.find_elements(By.XPATH, "//div[@role='article']//h3 | //div[contains(@class, 'fontHeadlineSmall')]")
        
        # If we didn't find elements with the above XPath, try the alternative
        if len(locationNames) == 0:
            locationNames = driver.find_elements(By.XPATH, "//a[@aria-label]")
        
        # Process the elements we found
        for ln in locationNames:
            # Get the location name (either from text or aria-label)
            if ln.text:
                locationName = ln.text
            else:
                locationName = ln.get_attribute('aria-label')
            
            # Only add if we haven't seen this location before
            if locationName and locationName not in seenLocations:
                seenLocations.add(locationName)
                allLocations.append(locationName)
                print(f"Found: {locationName}")
    
    return allLocations

allFoundLocs = scrollAndCollect(5)

print("\n--- All Collected Locations ---")
for i, location in enumerate(allFoundLocs):
    print(f"{i+1}. {location}")
# name = driver.find_elements(By.XPATH, '//a[@aria-label]')

# driver.close() # closes the browser 