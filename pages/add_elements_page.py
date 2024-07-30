from selenium.webdriver.common.by import By


class AddRemoveElements:
    def __init__(self,driver):
        self.driver = driver
        self.add_element_button = (By.XPATH,"//button[text()='Add Element']")
        self.delete_button = (By.XPATH,"//button[text()='Delete']")

    def click_add_element(self):
        self.driver.find_element(*self.add_element_button).click()

    def is_delete_present(self):
        if self.driver.find_element(*self.delete_button):
            return self.driver.find_element(*self.delete_button).is_displayed()
        return False
    
    def click_delete_button(self):
        self.driver.find_element(*self.delete_button).click()