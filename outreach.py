from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.youtube.com/")
time.sleep(2)
search = driver.find_element(By.NAME, "search_query")
search.send_keys("productivity tips")
search.send_keys(Keys.RETURN)
time.sleep(5)
channels = driver.find_elements(By.CSS_SELECTOR, "ytd-channel-name a")
creators =[]

for channel in channels[:10]:
    name = channel.text
    url = channel.get_attribute("href")
    if name and url:
        creators.append({"name": name, "about_url": url + "/about"})

with open("creators.csv","w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name","about_url"])
    writer.writeheader()
    writer.writerows(creators)

print(f"Saved {len(creators)} creators to creators.csv")

driver.quit()








