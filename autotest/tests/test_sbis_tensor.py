import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage

@pytest.mark.parametrize("url", ["https://sbis.ru", "https://tensor.ru"])
def test_open_site(browser, url):
    browser.get(url)

def test_sbis_to_tensor(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open_contacts()
    sbis_page.click_tensor_banner()

    tensor_page = TensorPage(browser)
    assert tensor_page.is_tensor_page_opened()

    tensor_page.click_people_power_link()
    assert tensor_page.is_about_page_opened()

    tensor_page.open_careers()
    tensor_page.verify_careers_photos_dimensions()
