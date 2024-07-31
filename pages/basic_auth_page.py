from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasicAuthPage:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get('https://the-internet.herokuapp.com/basic_auth')

    def submit_alert(self):
        self.alert = WebDriverWait(self.driver,10).until(EC.alert_is_present())
        # self.alert.send_keys('admin' + Keys.TAB + 'admin')
        # self.alert.accept()
        ActionChains(self.driver).send_keys('admin').send_keys(Keys.TAB).send_keys('admin').perform()
        self.alert.accept()
