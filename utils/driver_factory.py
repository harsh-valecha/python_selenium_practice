from selenium import webdriver
from selenium.webdriver import ChromeOptions , FirefoxOptions
from utils.config import Config

def get_driver():
    if Config.BROWSER == "chrome":
        return webdriver.Chrome(options=ChromeOptions())
    
    elif Config.BROWSER == "firefox":
        return webdriver.Firefox(options=FirefoxOptions())
    
    else:
        raise Exception(f"Browser {Config.BROWSER} is not supported.")
