import pytest
from pages.dropdown_page import DropdownPage

def test_dropdown(driver):
    dropdown = DropdownPage(driver)
    dropdown.select_by_value('1')
    dropdown.select_by_index('2')