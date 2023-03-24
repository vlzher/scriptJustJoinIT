import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from functools import lru_cache


@lru_cache(maxsize=None)
def scrape_urls():
    url = 'https://justjoin.it/?q=fullstack@keyword;Wroc%C5%82aw@city'
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)
    scrollable_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'css-ic7v2w'))
    )
    scroll_count = 0
    hrefs = []
    while scroll_count < 20:
        driver.execute_script("arguments[0].scrollBy(0, 500);", scrollable_div)
        time.sleep(1)
        hrefs_temp = [a.get_attribute('href') for a in scrollable_div.find_elements(By.TAG_NAME, 'a')]
        hrefs += hrefs_temp
        scroll_count += 1
    my_list = list(set(hrefs))
    driver.quit()
    return my_list
