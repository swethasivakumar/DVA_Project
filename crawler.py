from bs4 import BeautifulSoup
from contextlib import closing
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait

f = open("spoomovieCollections.txt",'a+')
fp = open("imdbtest.txt","r") 
baseURL = "http://www.imdb.com/title/"
parameters = "/business?ref_=tt_dt_bus"

with closing(Firefox()) as browser:
    for line in fp:
	finalURL = baseURL + str(line) + parameters
    	browser.get(finalURL)
    	def find(browser):
        	e = browser.find_element_by_id("tn15content")
        	if(e.text == "Calculating..."):
            		return False    
        	return e
    	e = WebDriverWait(browser, 20).until(find)
    	allText = e.text
    	allTextArray = allText.split('\n')
	collections = allTextArray[4].split()
    	f.write(collections[0])
	f.write("\n")
