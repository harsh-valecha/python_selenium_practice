import pytest
from pages.table_page import TablePage


@pytest.mark.skip
def test_table(driver):
    driver.get('https://the-internet.herokuapp.com/challenging_dom')
    table = TablePage(driver=driver)
    assert table.get_table_header()== True
    assert table.get_table_rows()==True