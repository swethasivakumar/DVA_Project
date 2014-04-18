from bs4 import BeautifulSoup
from contextlib import closing
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait

with closing(Firefox()) as browser:
    browser.get('http://www.imdb.com/title/tt0337978/business?ref_=tt_dt_bus')
    def find(browser):
        e = browser.find_element_by_id("tn15content")
        if(e.text == "Calculating..."):
            return False    
        return e
    e = WebDriverWait(browser, 20).until(find)
    allText = e.text
    allTextArray = allText.split('\n')
    print allTextArray[4]
