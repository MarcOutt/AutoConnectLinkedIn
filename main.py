import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from personnal_infos import email, password, phone_number

URL_FORMS = "https://docs.google.com/forms/d/e/1FAIpQLSfL8yeKQloKisBJBokmEW36elZ88UvhBsjSN9NO6w8HUvut6A/viewform?usp=sf_link"

EMAIL = email
PASSWORD = password
PHONE_NUMBER = phone_number


def initialize_driver():
    """
    Initialize a Chrome WebDriver instance and navigate to the LinkedIn login page.
    """
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_option)
    driver.get('https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fsearch%2Fresults'
               '%2FPEOPLE%2F%3Fkeywords%3Drecruteur%2520developpeurs%26origin'
               '%3DGLOBAL_SEARCH_HEADER%26sid%3DOlH&fromSignIn=true&trk=cold_join_sign_in')
    return driver


def cancel_cookies(driver):
    """
    Cancel cookies by clicking the deny button.
    """
    time.sleep(2)
    reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
    reject_button.click()


def fill_login_fields(driver):
    """
    Fill in the email and password fields on the LinkedIn login page.
    """
    time.sleep(5)
    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(EMAIL)
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(PASSWORD)


def click_apply_button(driver):
    """
    Click the "Apply" button on the LinkedIn login page.
    """
    apply_button = driver.find_element(By.CLASS_NAME, "btn__primary--large.from__button--floating")
    apply_button.click()


def main():
    """
    Main function to execute the LinkedIn automation script.
    """
    driver = initialize_driver()
    try:
        cancel_cookies(driver)
        fill_login_fields(driver)
        click_apply_button(driver)

        # Assuming manual CAPTCHA solving here
        input("Press Enter when you have solved the Captcha")

        page_number = 1
        while True:
            page_number += 1
            li_elements = driver.find_elements(By.CSS_SELECTOR, "li.reusable-search__result-container")
            for user in li_elements:
                button = user.find_element(By.CSS_SELECTOR, "button")
                if button.text == "Se connecter":
                    button.click()
                    driver.implicitly_wait(5)
                    send_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml1")
                    send_button.click()
                    print("Connected")

            try:
                next_page = driver.find_element(By.CSS_SELECTOR, f'button[aria-label="Page {page_number}"]')
                next_page.click()
                driver.implicitly_wait(5)
            except Exception as e:
                print(f"Error: {e}")
                raise  # Reraise the exception to close the browser

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

