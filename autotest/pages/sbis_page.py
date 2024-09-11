from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class SbisPage:
    def __init__(self, browser):
        self.browser = browser

    def open_contacts(self):
        contacts_link = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Контакты"))
        )
        contacts_link.click()

    def click_tensor_banner(self):
        tensor_banner = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'tensor.ru')]"))
        )
        tensor_banner.click()

    def is_tensor_page_opened(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[text()='Tensor']"))
            )
            return True
        except NoSuchElementException:
            return False

    def get_current_region(self):
        region_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='region-name']"))
        )
        return region_element.text

    def change_region(self, region_name):
        region_select = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='region-selector__button']"))
        )
        region_select.click()

        region_input = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@class='region-selector__input']"))
        )
        region_input.send_keys(region_name)
        region_input.send_keys(Keys.ENTER)

    def is_partners_list_present(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h3[text()='Партнеры']"))
            )
            return True
        except NoSuchElementException:
            return False

    def get_current_url(self):
        return self.browser.current_url

    def get_current_title(self):
        return self.browser.title