from selenium import webdriver # allows us to utilize a web browser for automation
from selenium.webdriver.common.keys import Keys # key logging
from selenium.webdriver.common.by import By # locates elements within a document

driver = webdriver.Chrome() # this will be the web browser that we are using for the automation process
driver.get("https://www.google.com/?client=safari") # link of the url that we will be automating

assert "Python" in webdriver.title # checks that the driver is using python?

element = driver.find_element(By.NAME, "q") # finds elements that are of the given argument
