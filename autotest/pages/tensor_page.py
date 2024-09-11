from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TensorPage:
    def __init__(self, browser):
        self.browser = browser

    def is_tensor_page_opened(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[text()='Tensor']"))
            )
            return True
        except NoSuchElementException:
            return False

    def click_people_power_link(self):
        link = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Подробнее"))
        )
        link.click()

    def is_about_page_opened(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[text()='О компании']"))
            )
            return True
        except NoSuchElementException:
            return False

    def open_careers(self):
        careers_link = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Работаем"))
        )
        careers_link.click()

    def verify_careers_photos_dimensions(self):
        photos = self.browser.find_elements(By.XPATH, "//div[@class='chronology-item']/div/img")
        first_photo_height = photos[0].size["height"]
        first_photo_width = photos[0].size["width"]
        for photo in photos:
            assert photo.size["height"] == first_photo_height
            assert photo.size["width"] == first_photo_width
