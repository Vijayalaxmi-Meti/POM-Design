from selenium.webdriver.common.by import By
from PageObjectClasses.base_page import BasePage

'''Search Results Page (search_results_page.py): Represents the search results page where we define actions like clicking on the first product (click_first_product). Uses try-except blocks to handle exceptions during element interactions.'''
class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.result_links = (By.CSS_SELECTOR, "div.s-result-item h2 a")

    '''try-except blocks to catch and print exceptions, ensuring that test failures due to unexpected errors are gracefully handled and reported.'''
    def click_first_product(self):
        try:
            self.click_element(self.result_links)
            return True
        except Exception as e:
            print(f"Exception occurred while clicking product: {str(e)}")
            return False
