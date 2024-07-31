from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username = (By.ID,"username")
        self.password = (By.ID,"password")
        self.loginbtn = (By.XPATH,"//button[@type='submit']")
        self.logoutbtn = (By.XPATH,"//a[@href='/logout']")
        self.flash= (By.ID,"flash")

    def click_login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.loginbtn).click()
        if 'logged into' in self.driver.find_element(*self.flash).text:
            return self.click_logout()
        else:
            return self.driver.find_element(*self.flash).text
        
    
    def click_logout(self):
        self.driver.find_element(*self.logoutbtn).click()
        return self.driver.find_element(*self.flash).text


    
    