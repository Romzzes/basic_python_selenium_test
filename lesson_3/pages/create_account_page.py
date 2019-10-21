class CreateAccount():
    def __init__(self, driver):
        self.driver = driver


    def fill_fields(self):
        first_name_field = self.driver.find_element_by_id("firstName")
        last_name_field = self.driver.find_element_by_id("lastName")
        password_field = self.driver.find_element_by_name("Passwd")
        confirm_password_field = self.driver.find_element_by_name("ConfirmPasswd")
        user_dictionary = {'fn': 'Roman', 'ln': 'Popov', 'password': 'Qwerty1234567890!'}

        first_name_field.send_keys(user_dictionary['fn'])
        last_name_field.send_keys(user_dictionary['ln'])
        password_field.send_keys(user_dictionary['password'])
        confirm_password_field.send_keys(user_dictionary['password'])

    def check_name(self, driver, email):
        validation_error = "Дозволені лише літери (a-z), числа (0-9) та крапки (.)."
        username_field = driver.find_element_by_id("username")
        next_button = driver.find_element_by_id("accountDetailsNext")
        username_field.clear()
        username_field.send_keys(email)
        next_button.click()
        time.sleep(1)
 #assert validation_error in driver.page_source