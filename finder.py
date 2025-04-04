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

from selenium import webdriver # imports the webdriver
from selenium.webdriver.common.keys import Keys # allows us to use input
from selenium.webdriver.common.by import By # 

# google maps url:  https://www.google.com/maps/@32.7678627,-117.0676283,3643m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MDMxOC4wIKXMDSoJLDEwMjExNjQwSAFQAw%3D%3D
url = 'https://www.google.com/maps/@32.7678627,-117.0676283,3643m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MDMxOC4wIKXMDSoJLDEwMjExNjQwSAFQAw%3D%3D'

# use a while loop to ask for the kind of input (zip code vs city)
# prototype implementation

type = ''
while type != 'CITY' or type != 'ZIP CODE':
    type = input("Enter if you are searching by CITY or ZIP CODE")

if type == 'CITY': # if it equals to city, use the city as the input for our method
    pass
else: # else if not city, we will pass in the zipcode
    pass

# prompt the user for what they are searching for in the area
reason = ''
while reason == '':
    reason = input(f'What are you searching for in {type}')

driver = webdriver.Chrome() # browser to use
driver.get(url)

driver.implicitly_wait(5) # using an implicit wait to help us sync browser and code so that it does not return an exception



# temp implementation of passing in CITY or ZIP CODE
# ex. VARIABLE.send_keys('REASON in CITY/ZIP CODE')

# create a list of locations            
# filter by class name or class ID

driver.close() # closes the browser