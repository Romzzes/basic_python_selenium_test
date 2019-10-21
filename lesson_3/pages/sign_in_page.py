class SignInPage():
    def __init__(self, driver):
        self.driver = driver

    def account_create_button(self):
        import time
        create_account_button = self.driver.find_element_by_xpath("//*[text()='Створити обліковий запис']")
        create_account_button.click()
        time.sleep(2)
        for_myself_button = self.driver.find_element_by_xpath("//*[text()='Для себе']")
        for_myself_button.click()


