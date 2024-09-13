import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_sbis_download(browser):
    # 1. Перейти на https://sbis.ru/
    browser.get("https://sbis.ru/")

    # 2. Найти и перейти "Скачать локальные версии" в Footer'e
    download_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Скачать локальные версии')]"))
    )
    download_link.click()

    # 3. Скачать СБИС Плагин для Windows, веб-установщик
    plugin_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'СБИС Плагин')]"))
    )
    plugin_link.click()

    # 4. Убедиться, что плагин скачался
    download_path = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(download_path, exist_ok=True)

    # Ожидание скачивания файла
    time.sleep(5) # Временно, замените более точным ожиданием, если это возможно

    # 5. Сравнить размер скачанного файла в мегабайтах
    downloaded_file = os.listdir(download_path)[0]
    downloaded_file_size_mb = os.path.getsize(os.path.join(download_path, downloaded_file)) / (1024 * 1024)

    # Сравнение с ожидаемым размером
    expected_file_size_mb = 3.64
    assert round(downloaded_file_size_mb, 2) == expected_file_size_mb
