import pytest
from selenium import webdriver
from utils.driver_factory import get_driver
import os
import pytest_html

@pytest.fixture(scope='session')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


