from selenium.webdriver.common.by import By

class CheckboxPage:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get('https://the-internet.herokuapp.com/checkboxes')
        self.checkbox1 = (By.XPATH,"//input[position()=1]")
        self.checkbox2 = (By.XPATH,"//input[position()=1]")

    def is_checkbox1_active(self):
        return self.driver.find_element(*self.checkbox1).is_selected()
    
    def is_checkbox2_active(self):
        return self.driver.find_element(*self.checkbox2).is_selected()
    
    def click_checkbox1(self):
        self.driver.find_element(*self.checkbox1).click()

    def click_checkbox2(self):
        self.driver.find_element(*self.checkbox2).click()
