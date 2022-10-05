from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest

@pytest.fixture()
def input_password(browser):
    username = WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
    input_password = username.find_element(By.CSS_SELECTOR, "input")
    return input_password

def test_do_not_enter_password(browser, input_password):
    input_password.send_keys("")
    error_message = browser.find_element(By.ID, "password").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    
    assert error_message == "Введите пароль", f"Wrong error message. Received message: '{error_message}'"

def test_enter_valid_password_format(browser, input_password):
    input_password.send_keys("password")
    try:
        error_message = browser.find_element(By.ID, "password").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    except NoSuchElementException:
        error_message = ""
    
    assert error_message == "", f"Wrong error message. Received message: '{error_message}'"

def test_show_password_after_typing(browser, input_password):
    input_password.send_keys("password")
    button_view = browser.find_element(By.ID, "password").find_element(By.CSS_SELECTOR, "button.icon-button.ng-star-inserted")
    button_view.click()
    input_password_attribures = browser.execute_script("""
                                                       let attr = arguments[0].attributes;
                                                       let items = {}; 
                                                       for (let i = 0; i < attr.length; i++) {
                                                           items[attr[i].name] = attr[i].value;
                                                           }
                                                        return items;
                                                        """, input_password)
    assert input_password_attribures["type"] == "text", f"Show password button not working: '{input_password_attribures['type']}'"