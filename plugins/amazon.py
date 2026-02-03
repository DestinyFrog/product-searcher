from searcher import Searcher

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

class SearcherAmazon(Searcher):
    def get_service(self):
        return "Amazon"

    def get_url(self):
        return "https://www.amazon.com.br/"
    
    def search_cards(self, driver):
        wait = WebDriverWait(driver, 10)

        wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.send_keys(self.search_term + Keys.ENTER)

        time.sleep(1)
        product_cards = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

        data = []
        for card in product_cards:
            try:
                content = card.find_element(By.XPATH, "//div[@data-cy='title-recipe']")

                link = content.find_element(By.TAG_NAME, "a")
                str_link = link.get_attribute("href")
                
                title = content.find_element(By.TAG_NAME, "h2")
                str_title = title.text

                content_price = card.find_element(By.XPATH, "//div[@data-cy='price-recipe']")
                a_price = content_price.find_element(By.CLASS_NAME, "a-price")
                num_price = a_price.text

                data.append({
                    "price": num_price,
                    "title": str_title,
                    "link": str_link,
                    "service": self.get_service()
                })
            except:
                pass

        return data