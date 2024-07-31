from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DropdownPage:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get('https://the-internet.herokuapp.com/dropdown')
        self.dropdown = (By.ID,"dropdown")

    def select_by_value(self,value):
        dropdown = Select(self.driver.find_element(*self.dropdown))
        dropdown.select_by_value(value)
        WebDriverWait(driver = self.driver,timeout=10).until(
            EC.text_to_be_present_in_element_value(self.dropdown,value)
        )
        

    def select_by_index(self,index):
        dropdown = Select(self.driver.find_element(*self.dropdown))
        dropdown.select_by_index(index)
        WebDriverWait(driver=self.driver,timeout=10).until(
            EC.text_to_be_present_in_element_attribute(self.dropdown,'value',index)
        )
        
