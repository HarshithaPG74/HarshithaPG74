from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pynput.keyboard import Key,Controller

driver = webdriver.Chrome()
driver.get("test123")
time.sleep(2)
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("test11")
driver.find_element(By.XPATH,"//input[@data-placeholder='Please enter password']").send_keys("test@11")
driver.find_element(By.XPATH,"//span[@class='mat-button-wrapper']").click()

dashboard=driver.find_element(By.XPATH,"//textarea[@placeholder='Enter multiple styles or ecodes separated by commas, semi-colons, or line breaks']")
dashboard.send_keys("10472649")
time.sleep(5)
driver.find_element(By.XPATH,"//span[normalize-space()='Add styles to Worklist']").click()
driver.find_element(By.XPATH, "//span[text()='Close']").click()
#driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator mt-btn-primary mat-button mat-button-base']").click()

driver.find_element(By.XPATH,"//a[normalize-space()='10472649']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//h3[normalize-space()='DAM Tray']").click()
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("Yes I Scrolled till end")
#driver.find_element(By.XPATH,"//button[@aria-label='Last page']//span[@class='mat-button-wrapper']//*[name()='svg']")
time.sleep(3)
element1=driver.find_element(By.XPATH,"//li[@class='mt-thumbnail ng-star-inserted'][1]")
print("Hiiiii")
element2=driver.find_element(By.XPATH,"(//input[@id='fileDropRef'])[1]")

act = ActionChains(driver)

act.drag_and_drop(element1,element2).perform()
time.sleep(15)
