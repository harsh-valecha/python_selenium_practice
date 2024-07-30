import pytest
from pages.checkbox_page import CheckboxPage

def test_checkboxes(driver):
    checkbox = CheckboxPage(driver)
    checkbox.click_checkbox1()
    assert checkbox.is_checkbox1_active()==True
    if checkbox.is_checkbox2_active():
        checkbox.click_checkbox2()
        assert checkbox.is_checkbox2_active()==False