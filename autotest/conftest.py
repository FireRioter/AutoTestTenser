import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome() # Используйте нужный драйвер (Chrome, Firefox, ...)
    driver.maximize_window() # (Optional) Развернуть браузер на весь экран
    yield driver
    driver.quit()
