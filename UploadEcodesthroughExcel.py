import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Read data from Excel
excel_file = 'styles.xlsx'  # Your Excel file
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook.active

# Assuming the style codes are in the first column (A)
style_codes = [cell.value for cell in sheet['A'] if cell.value is not None]

# Step 2: Set up Selenium
driver = webdriver.Chrome()  # Make sure to have the ChromeDriver installed
driver.get('test123')  # Replace with your web application URL
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("test344")
driver.find_element(By.XPATH,"//input[@data-placeholder='Please enter password']").send_keys("test@9876")
driver.find_element(By.XPATH,"//span[@class='mat-button-wrapper']").click()
time.sleep(3)
# Locate the textbox (adjust the locator as necessary)
textbox = driver.find_element(By.XPATH,"//textarea[@placeholder='Enter multiple styles or ecodes separated by commas, semi-colons, or line breaks']")
  # Replace with actual ID
#This is modified git
for code in style_codes:
    textbox.clear()  # Clear the textbox if needed
    textbox.send_keys(code)  # Send the style code
    #textbox.send_keys(Keys.RETURN)  # Optional: Submit if needed

    #if driver.find_element(By.XPATH,"//td[normalize-space()='Already present in your list']"):
    time.sleep(1)  # Wait for any loading or processing
    driver.find_element(By.XPATH, "//span[normalize-space()='Add styles to Worklist']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[text()='Close']").click()
    time.sleep(2)


driver.find_element(By.XPATH,"//a[normalize-space()='FQ1759106']").click()

# Close the browser after the operation
driver.quit()
