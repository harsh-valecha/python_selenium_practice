import pytest
from pages.basic_auth_page import BasicAuthPage

@pytest.mark.xfail
def test_basic_auth(driver):
    Auth = BasicAuthPage(driver=driver)
    Auth.submit_alert()