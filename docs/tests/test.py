
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Test cases: Browse catalog and search for a book
def test_browsing_search():

    print("Browsing and search test cases to be implemented.")  
    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:3000/catalog")

        #Search book by full title
        time.sleep(2)  
        search_full_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'search'))
        )
        search_full_title.send_keys("To Kill a Mockingbird")

        #Search using partial keyword
        time.sleep(2)
        search_full_title.clear()
        search_partial_keyword = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'search'))
        )
        search_partial_keyword.send_keys("Kill")

        #Search case-insensitive
        time.sleep(2)
        search_partial_keyword.clear()
        search_case_insensitive = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'search'))
        )
        search_case_insensitive.send_keys("The Great Gatsby")
        time.sleep(2)
        search_case_insensitive.clear()
        search_case_insensitive.send_keys("the great gatsby")

        #Search by Author Name
        time.sleep(2)
        search_case_insensitive.clear()
        search_author = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'search'))
        )
        search_author.send_keys("Harper Lee")

        #Search nonexistent Book
        time.sleep(2)
        search_author.clear()
        search_nonexistent = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'search'))
        )
        search_nonexistent.send_keys("Harry Potter")

    finally:
        #close the browser
        input("Press Enter to close the browser...")
        driver.quit()


#Test cases: Add items to cart and proceed to checkout-- Shopping Cart
def shopping_cart():

    print("Shopping cart test cases to be implemented.")
    driver = webdriver.Chrome()
      
    try:
        driver.get("http://localhost:3000")

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

        #Update Quantity
        time.sleep(2)
        update_quantity = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div[1]/div[2]/input'))
        )
        update_quantity.clear()
        update_quantity.send_keys("4")

        #Remove item from cart
        time.sleep(2)
        remove_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div[1]/div[2]/button'))  
        )
        remove_item.click()

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

        #Pay Now button
        time.sleep(2)
        paynow_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div/div/button[2]'))
        )
        paynow_button.click()

        
    finally:
        #close the browser
        input("Press Enter to close the browser...")
        driver.quit()

#Card Payment Test Cases-- PAYSTACK
def card_payment():

    print("Card payment test cases to be implemented.")
    driver = webdriver.Chrome()
    
    try:
        driver.get("http://localhost:3000/checkout")

        time.sleep(2)
        paynow_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div/section/div/div/div[1]/nav/div/ul/li[4]/a'))
        )
        paynow_button.click()
        
        #Switch into Paystack iframe
        time.sleep(2)
        iframe = WebDriverWait(driver, 30).until(
           EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        driver.switch_to.frame(iframe)
        print("Switched to Paystack iframe.")

        time.sleep(3)
        # Select a test card (successful card) from the list
        card_option = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/nav/div/ul/li[1]/a'))
        )
        card_option.click()
        print("Clicked Card option.")

        #Successful option
        time.sleep(2)
        successful_option = WebDriverWait(driver, 10).until(
              EC.element_to_be_clickable((By.XPATH, '//*[@id="test-cards"]/div[1]/div[1]/div'))
          )
        successful_option.click()
        time.sleep(2)
        pay_card_button = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, '//*[@id="test-cards"]/button'))
        )
        pay_card_button.click()
      

        #Authentication option
        time.sleep(2)
        shopping_cart()
        authentication = WebDriverWait(driver, 10).until(
              EC.element_to_be_clickable((By.XPATH, '//*[@id="test-cards"]/div[1]/div[2]/div'))
          )
        authentication.click()
        pay_card_button = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, '//*[@id="test-cards"]/button'))
        )
        pay_card_button.click()

        #Decline option
        time.sleep(2)
        shopping_cart()
        decline = WebDriverWait(driver, 10).until(
              EC.element_to_be_clickable((By.XPATH, '//*[@id="test-cards"]/div[1]/div[3]/div'))
          )
        decline.click()
        pay_card_button = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, '//*[@id="test-cards"]/button'))
        )
        pay_card_button.click()
        

       
    finally:
        input("Press Enter to close the browser...")
        driver.quit()


#EFT Payment Test Cases -- PAYSTACK
def eft_payment():

    print("EFT payment test cases to be implemented.")
    driver = webdriver.Chrome()
    
    try:

        driver.get("http://localhost:3000/checkout")

        shopping_cart()

        time.sleep(2)
        eft_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/section/div/div/div[1]/nav/div/ul/li[4]/a'))
        )
        eft_button.click()

        time.sleep(1)
        authenticate_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="payment-form"]/div/div/div[2]/button'))
        )
        authenticate_button.click()

        time.sleep(1)
        test_successful = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="select-testSuccessfulResponse"]'))
        )
        test_successful.click()




    

    finally:
       
        input("Press Enter to close the browser...")
        driver.quit()


  

#Calling the above functions
#Test_browsing_search()
#shopping_cart()
#card_payment()
eft_payment()