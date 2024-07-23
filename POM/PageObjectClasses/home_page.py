from selenium.webdriver.common.by import By
from PageObjectClasses.base_page import BasePage
from PageObjectClasses.search_results_page import SearchResultsPage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")

    '''Home Page (home_page.py): Represents the Amazon home page and includes methods specific to performing a search (search_for_product).'''
    ''' Uses try-except blocks to catch and handle exceptions gracefully.'''

    def search_for_product(self, keyword):
        try:
            self.enter_text(self.search_box, keyword)
            self.click_element(self.search_button)
            return SearchResultsPage(self.driver)
        except Exception as e:
            print(f"Exception occurred while searching: {str(e)}")
            return None
