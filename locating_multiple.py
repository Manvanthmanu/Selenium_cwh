from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
for p in range(1,20):
    driver.get(f"https://www.amazon.com/s?k={query}&page={p}&ref=nav_bb_sb")

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f'{len(elems)} items found')
    for elem in elems:
        print(elem.text)
# print(elem.get_attribute('outerHTML'))
# print(elem.text)

time.sleep(4)


driver.close()