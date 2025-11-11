from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_selenium_bookstore():

    driver = webdriver.Chrome()
    
    try:
        driver.get("http://localhost:3000/catalog")

        #Add books to cart
        time.sleep(2)  
        add_item1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/main/div[2]/div[2]/div/div/button'))
        )
        add_item1.click()

        time.sleep(2)
        add_item2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/main/div[2]/div[1]/div/div/button'))
        )
        add_item2.click()


        #Go to cart
        time.sleep(2)
        cart_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/cart"]'))
        )
        cart_icon.click()

        time.sleep(3)
        proceed_to_checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/checkout"]'))
        )
        proceed_to_checkout_button.click()

        #Checkout Form Filling
        time.sleep(2)
        fullname_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'fullName'))
        )
        fullname_input.send_keys("Thembisile Nkambule")

        time.sleep(1)
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        email_input.send_keys("thembisile@gmail.com")

        time.sleep(1)
        address_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'address'))
        )
        address_input.send_keys("7 Poplar Ave")

        time.sleep(1)
        city_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'city'))
        )
        city_input.send_keys("Nelspruit")

        time.sleep(1)
        country_input =WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'country'))
        )
        country_input.send_keys("South Africa")

        time.sleep(1)
        postal_code_input =WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'postalCode'))
        )
        postal_code_input.send_keys("0458")

        time.sleep(2)
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/form/div[5]/button'))
        )
        next_button.click()

        #Payment Process
        time.sleep(3)
        proceed_payment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div/div[2]/button[2]'))
        )
        proceed_payment_button.click()

        time.sleep(2)
        paynow_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div/div/button[2]'))
        )
        paynow_button.click()



    
    finally:
        #close the browser
        input("Press Enter to close the browser...")
        driver.quit()

test_selenium_bookstore()