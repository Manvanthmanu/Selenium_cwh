from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file = 0
for p in range(1,10):
    # driver.get(f"https://www.amazon.com/s?k={query}&page={p}&ref=nav_bb_sb")
    # driver.get(f"https://www.amazon.de/s?k=LAPTOP&crid=1D1FBPR93YL96&sprefix={query}%2Caps%2C349&ref=nb_sb_noss_1")
    driver.get(f"https://www.amazon.de/-/en/s?k={query}&page={p}&crid=1D1FBPR93YL96&qid=1719650369&sprefix=laptop%2Caps%2C349&ref=sr_pg_2")

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f'{len(elems)} items found')
    for elem in elems:
        d = elem.get_attribute('outerHTML')
        with open(f"data\\{query}_{file}.html","w", encoding="utf-8") as f:
            f.write(d)
            file += 1
# print(elem.get_attribute('outerHTML'))
# print(elem.text)

time.sleep(4)


driver.close()