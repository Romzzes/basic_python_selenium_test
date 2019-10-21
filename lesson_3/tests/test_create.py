from selenium import webdriver
from lesson_3.pages.sign_in_page import SignInPage
from lesson_3.pages.create_account_page import CreateAccount

driver = webdriver.Chrome("C:/Users/r.popov/Desktop/python course/chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https://accounts.google.com")

sign_in_page = SignInPage(driver)
create_account_page = CreateAccount(driver)

sign_in_page.account_create_button()
create_account_page.fill_fields()
email_list = ['@a.a', 'a@-a.a', 'a@a@a', 'a@a']

for email in email_list:
    create_account_page.check_name(driver, email)

driver.quit()