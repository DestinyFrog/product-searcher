from searcher import Searcher

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import re

class SearcherMercadoLivre(Searcher):
    def get_service(self):
        return "Mercado Livre"

    def get_url(self):
        return "https://www.mercadolivre.com.br/"
    
    def search_cards(self, driver):
        wait = WebDriverWait(driver, 10)

        search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Buscar produtos, marcas e muito mais…']")
        search_bar.send_keys(self.search_term + Keys.ENTER)

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        product_cards = driver.find_elements(By.CLASS_NAME, "ui-search-layout__item")

        data = []
        for card in product_cards:
            try :
                title = card.find_element(By.CSS_SELECTOR, ".poly-component__title")
                price = card.find_element(By.CSS_SELECTOR, ".poly-price__current")

                no_space_price = price.text.replace("\n", "")
                h_price = re.findall(r"\d+,\d\d", no_space_price)

                num_price = float(h_price[0].replace(",", "."))
                str_title = title.text.replace("\n", "")
                str_link = title.get_attribute("href")

                data.append({
                    "price": num_price,
                    "title": str_title,
                    "link": str_link,
                    "service": self.get_service()
                })
            except:
                pass

        return data