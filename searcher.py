from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from thefuzz import fuzz

class Searcher:
    def __init__(self):
        self.search_term = None

    def set_search_term(self, search_term):
        self.search_term = search_term
        return self

    def get_url(self):
        return ""
    
    def search(self):
        driver = None
        data = None
        
        try:
            if not self.search_term:
                raise Exception('Search term is not defined')

            driver = webdriver.Chrome()
            url = self.get_url()
            driver.get(url)
            data = self.search_cards(driver)
            sorted_data_by_name = self.sort_by_name(data)
            return sorted_data_by_name

        except Exception as err:
            raise err

        finally:
            if driver:
                driver.quit()

    def search_cards(self, driver):
        return None

    def sort_by_name(self, data):
        def get_score(product):
            score = fuzz.token_sort_ratio(product['title'], self.search_term)
            return score

        return sorted(data, key=lambda product: get_score(product), reverse=True)
