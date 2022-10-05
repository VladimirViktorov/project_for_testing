from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def test_do_not_enter_password(browser):
    username = WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
    input_login = username.find_element(By.CSS_SELECTOR, "input")
    input_login.send_keys('')
    error_message = username.find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    
    assert error_message == "Введите пароль", f"Wrong error message. Received message: '{error_message}'"

def test_enter_valid_password_format(browser):
    username = WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
    input_login = username.find_element(By.CSS_SELECTOR, "input")
    input_login.send_keys('as@mail.ru')
    try:
        error_message = username.find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    except NoSuchElementException:
        error_message = ""
    
    assert error_message == "", f"Wrong error message. Received message: '{error_message}'"

def test_show_password_after_typing(browser):
    username = WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
    input_login = username.find_element(By.CSS_SELECTOR, "input")
    input_login.send_keys('as@mail.ru')
    try:
        error_message = username.find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    except NoSuchElementException:
        error_message = ""
    
    assert error_message == "", f"Wrong error message. Received message: '{error_message}'"