import time
from selenium import webdriver
from bs4 import BeautifulSoup
from functools import lru_cache


@lru_cache(maxsize=None)
def count_div_occurrences(links):
    counts = {}
    driver = webdriver.Chrome()

    for link in links:
        driver.get(link)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        divs = soup.find_all('div', {'class': 'css-1xm32e0'})
        for div in divs:
            title = div.get('title', '')
            if title in counts:
                counts[title] += 1
            else:
                counts[title] = 1

    driver.quit()

    return counts
