from selenium import webdriver
from selenium.webdriver import ChromeOptions , FirefoxOptions
from utils.config import Config

def get_driver():
    if Config.BROWSER == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=1')
        return webdriver.Chrome(options=options)
    
    elif Config.BROWSER == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('--log-level=1')
        return webdriver.Firefox(options=options)
    
    else:
        raise Exception(f"Browser {Config.BROWSER} is not supported.")
