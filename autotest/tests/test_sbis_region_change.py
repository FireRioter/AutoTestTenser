import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.sbis_page import SbisPage

@pytest.mark.parametrize("expected_region", ["Ярославская обл.", "Камчатский край"])
def test_sbis_region_change(browser, expected_region):
    sbis_page = SbisPage(browser)
    sbis_page.open_contacts()

    # Проверка начального региона
    initial_region = sbis_page.get_current_region()
    assert initial_region == "Ярославская обл."
    assert sbis_page.is_partners_list_present()

    # Изменение региона
    sbis_page.change_region(expected_region)

    # Проверка изменения региона
    changed_region = sbis_page.get_current_region()
    assert changed_region == expected_region

    # Проверка списка партнеров
    assert sbis_page.is_partners_list_present()

    # Проверка URL и заголовка
    assert expected_region in sbis_page.get_current_url()
    assert expected_region in sbis_page.get_current_title()
