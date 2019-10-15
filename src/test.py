from selenium import webdriver

driver = webdriver.Chrome("C:/Users/r.popov/Desktop/python course/chromedriver.exe")

driver.get("https://www.wikipedia.org/")

search_field = driver.find_element_by_id("searchInput")
search__button = driver.find_element_by_xpath("//form[@id = 'search-form']/fieldset/button")

search_field.send_keys("Test Automation")
search__button.click()

assert "Test automation" in driver.title
assert "Test 1 automation" in driver.title
assert "Test 2 automation" in driver.title

driver.quit()