from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
NICHES = [
    "productivity",
    "personal finance",
    "entrepreneurship",
    "self improvement",
    "tech tutorials"




    ]
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
all_creators =[]
seen_urls = set()

for niche in NICHES:
    print(f'Searching for{niche}')
    driver.get("https://www.youtube.com")
    time.sleep(2)

    search = driver.find_element(By.NAME,"search_query")
    search.clear()
    search.send_keys(niche)
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    channels = driver.find_elements(By.CSS_SELECTOR, "ytd-channel-name a")

    for channel in channels[:10]:
        name = channel.text
        url = channel.get_attribute("href")
        if name and url and url not in seen_urls:
            seen_urls.add(url)
            all_creators.append({"name": name, "about_url": url + "/about", "niche": niche})
driver.quit()


with open("creators.csv","w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name","about_url","niche"])

    writer.writeheader()
    writer.writerows(all_creators)

print(f"Saved {len(all_creators)} unique  creators to creators.csv")










