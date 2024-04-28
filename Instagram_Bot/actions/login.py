from tools.selenium_functions import name, xpath
import web_elements.instagram as style
from web_elements.instagram import name_username, name_password, xpath_login
from selenium.common.exceptions import TimeoutException


def login(params, url_case):
    url, user, password, browser = [*params]

    browser.get(url)
    
    try:
        login_input = name(name_username[url_case], browser)
        login_input.send_keys(user)

        password_input = name(name_password[url_case], browser)
        password_input.send_keys(password)

        login_btn = xpath(xpath_login[url_case], browser)
        login_btn.click()      
        try:
            validation_input = xpath(style.xpath_validation, browser)
            validation_input.click()

            confirmation_code = input("Validation code: ")

            login_input = xpath(style.xpath_input_code, browser)
            login_input.send_keys(confirmation_code)

            validation_submit = xpath(style.xpath_btn_submit, browser)
            validation_submit.click()

            not_now_btn = xpath(style.xpath_not_now, browser)
            not_now_btn.click()
        except TimeoutException:
            try:
                save_password_not_now = xpath(
                    style.xpath_save_password_not_now, browser
                )
                save_password_not_now.click()

                notification_not_now = xpath(style.xpath_notification_not_now, browser)
                notification_not_now.click()
            except TimeoutException:
                notification_not_now = xpath(style.xpath_notification_not_now, browser)
                notification_not_now.click()

                save_password_not_now = xpath(
                    style.xpath_save_password_not_now, browser
                )
                save_password_not_now.click()

    except TimeoutException:
        print("Problema de TimeoutException, no arquivo action/login.py")
        