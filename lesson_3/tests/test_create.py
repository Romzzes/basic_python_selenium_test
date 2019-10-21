from selenium import webdriver
from lesson_3.pages.sign_in_page import SignInPage
from lesson_3.pages.create_account_page import CreateAccountPage

driver = webdriver.Chrome("C:/Users/r.popov/Desktop/python course/chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https://accounts.google.com")

sign_in_page = SignInPage(driver)
create_account_page = CreateAccountPage(driver)

sign_in_page.create_account_button_click()
sign_in_page.for_myself_button_click()
create_account_page.determine_variables()
email_list = ['@a.a', 'a@-a.a', 'a@a@a', 'a@a']

for email in email_list:
    create_account_page.validate_username_field(driver, email)

driver.quit()