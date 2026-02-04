from selenium import webdriver

from models.products import Product

class Searcher:
    def __init__(self):
        self.search_term = None
        self.min_score = 25
        self.products = []

    def set_search_term(self, search_term):
        self.search_term = search_term
        return self

    def get_url(self):
        return ""
    
    def search(self, driver):
        data = None
        
        try:
            if not self.search_term:
                raise Exception('Search term is not defined')
            
            if not driver:
                driver = webdriver.Chrome()

            url = self.get_url()
            driver.get(url)
            data = self.search_cards(driver)
            self.products = data

        except Exception as err:
            raise err
        return self

    def search_cards(self, driver):
        return None
    
    def save(self):
        for product in self.products:
            Product.create(
                title   = product['title'],
                link    = product['link'],
                service = product['service'],
                price   = product['price'],
                score   = product['score'],
                term    = self.search_term)