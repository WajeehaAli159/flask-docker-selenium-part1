from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        options=options
    )
    return driver


def test_app_loads():
    driver = get_driver()
    driver.get("http://users:5000")
    assert driver.title is not None
    driver.quit()


def test_title_exists():
    driver = get_driver()
    driver.get("http://users:5000")
    assert driver.title != ""
    driver.quit()


def test_url_correct():
    driver = get_driver()
    driver.get("http://users:5000")
    assert "users" in driver.current_url
    driver.quit()


def test_body_tag_exists():
    driver = get_driver()
    driver.get("http://users:5000")
    body = driver.find_element(By.TAG_NAME, "body")
    assert body is not None
    driver.quit()


def test_html_loaded():
    driver = get_driver()
    driver.get("http://users:5000")
    html = driver.find_element(By.TAG_NAME, "html")
    assert html is not None
    driver.quit()

