from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.onet.pl')
assert 'Onet' in browser.title

elem = browser.find_element_by_name('qt')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

#browser.quit()
