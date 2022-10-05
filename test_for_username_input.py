from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest

@pytest.fixture()
def input_login(browser):
    username = WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
    input_login = username.find_element(By.CSS_SELECTOR, "input")
    return input_login

@pytest.mark.parametrize('email', ["@mail.ru", 
                                  f"{'m'*81}@mail.ru",
                                  "mail@.ru",
                                  f"mail@{'m'*81}.ru",
                                  "mail@mail.",
                                  "mail@mail.r",
                                  f"mail@mail.{'r'*21}"])
def test_enter_invalid_email_format(browser, input_login, email):
    input_login.send_keys(email)
    error_message = browser.find_element(By.ID, "username").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    
    assert error_message == "Введенный email имеет недопустимый формат", f"Wrong error message. Received message: '{error_message}'"

def test_do_not_enter_email(browser, input_login):
    input_login.send_keys('')
    error_message = browser.find_element(By.ID, "username").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    
    assert error_message == "Введите email", f"Wrong error message. Received message: '{error_message}'"

@pytest.mark.parametrize('email', ["m@mail.ru", 
                                  f"{'m'*80}@mail.ru",
                                  "mail@m.ru",
                                  f"mail@{'m'*80}.ru",
                                  "mail@mail.ru",
                                  f"mail@mail.{'r'*20}"])
def test_enter_valid_email_format(browser, input_login, email):
    input_login.send_keys(email)
    try:
        error_message = browser.find_element(By.ID, "username").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    except NoSuchElementException:
        error_message = ""
    
    assert error_message == "", f"Wrong error message. Received message: '{error_message}'"