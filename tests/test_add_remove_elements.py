import pytest
from utils.config import Config
from pages.add_elements_page import AddRemoveElements


def test_add_elements(driver):
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    elements = AddRemoveElements(driver=driver)
    elements.click_add_element()
    assert elements.is_delete_present()== True
    elements.click_delete_button()
    assert elements.is_delete_present()==False


