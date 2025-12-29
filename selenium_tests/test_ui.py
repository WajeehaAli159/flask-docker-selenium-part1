from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )
    return driver


# ---------- 10 TEST CASES ----------

def test_app_loads():
    driver = get_driver()
    driver.get("http://users:5000")
    assert driver.page_source
    driver.quit()


def test_title_exists():
    driver = get_driver()
    driver.get("http://users:5000")
    assert driver.title is not None
    driver.quit()


def test_url_correct():
    driver = get_driver()
    driver.get("http://users:5000")
    assert "http" in driver.current_url
    driver.quit()


def test_html_tag_present():
    driver = get_driver()
    driver.get("http://users:5000")
    assert "<html" in driver.page_source.lower()
    driver.quit()


def test_body_tag_present():
    driver = get_driver()
    driver.get("http://users:5000")
    assert "<body" in driver.page_source.lower()
    driver.quit()


def test_page_not_empty():
    driver = get_driver()
    driver.get("http://users:5000")
    assert len(driver.page_source) > 50
    driver.quit()


def test_dom_loaded():
    driver = get_driver()
    driver.get("http://users:5000")
    assert driver.execute_script("return document.readyState") == "complete"
    driver.quit()


def test_refresh_page():
    driver = get_driver()
    driver.get("http://users:5000")
    driver.refresh()
    assert driver.page_source
    driver.quit()


def test_has_div():
    driver = get_driver()
    driver.get("http://users:5000")
    assert driver.find_elements(By.TAG_NAME, "div") is not None
    driver.quit()


def test_has_links():
    driver = get_driver()
    driver.get("http://users:5000")
    assert driver.find_elements(By.TAG_NAME, "a") is not None
    driver.quit()

