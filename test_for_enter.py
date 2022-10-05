from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def filling_form(browser, login_text, password_text):
    username = WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
    login = username.find_element(By.CSS_SELECTOR, "input")
    login.send_keys(login_text)
    password = browser.find_element(By.ID, "password").find_element(By.CSS_SELECTOR, "input")
    password.send_keys(password_text)
    button = browser.find_element(By.CSS_SELECTOR, "button.ui.primary.button.ng-tns-c188-0")
    button.click()

def test_empty_form_check_login(browser):
    filling_form(browser, "", "")
    error_message_login = browser.find_element(By.ID, "username").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    
    assert error_message_login == "Введите email", f"Wrong error message. Received message: '{error_message_login}'"

def test_empty_form_check_password(browser):
    filling_form(browser, "", "")
    error_message_password = browser.find_element(By.ID, "password").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    
    assert error_message_password == "Введите пароль", f"Wrong error message. Received message: '{error_message_password}'"

def test_fill_login_do_not_fill_password_check_login(browser):
    filling_form(browser, "mail@mail.ru", "")
    try:
        error_message_login = browser.find_element(By.ID, "username").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    except NoSuchElementException:
        error_message_login = ""
    
    assert error_message_login == "", f"Wrong error message. Received message: '{error_message_login}'"

def test_fill_login_do_not_fill_password_check_password(browser):
    filling_form(browser, "mail@mail.ru", "")
    error_message_password = browser.find_element(By.ID, "password").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    
    assert error_message_password == "Введите пароль", f"Wrong error message. Received message: '{error_message_password}'"

def test_do_not_fill_login_fill_password_check_login(browser):
    filling_form(browser, "", "password")
    error_message_login = browser.find_element(By.ID, "username").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    
    assert error_message_login == "Введите email", f"Wrong error message. Received message: '{error_message_login}'"

def test_do_not_fill_login_fill_password_check_password(browser):
    filling_form(browser, "", "password")
    try:
        error_message_password = browser.find_element(By.ID, "password").find_element(By.CSS_SELECTOR, "ui-field-error.ng-star-inserted").text
    except NoSuchElementException:
        error_message_password = ""
    
    assert error_message_password == "", f"Wrong error message. Received message: '{error_message_password}'"