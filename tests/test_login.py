import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize('username,password',[('tomsmith','SuperSecretPassword!')])
def test_login_positive(driver,username,password):
    driver.get('https://the-internet.herokuapp.com/login')
    login = LoginPage(driver=driver)
    assert 'logged out ' in login.click_login(username=username,password=password)
    

@pytest.mark.parametrize('username,password',[('kamlesh','chattu')])
def test_login_negative(driver,username,password):
    driver.get('https://the-internet.herokuapp.com/login')
    login = LoginPage(driver=driver)
    assert 'invalid!' in login.click_login(username=username,password=password)
    


    


