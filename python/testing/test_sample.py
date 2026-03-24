import os
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def test_addition():
    assert 2 + 3 == 5

def test_one():
    assert 5 > 1

def test_two():
    assert 3 * 2 == 6

def test_division():
    assert 6/2 == 3 

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    d = webdriver.Chrome(options=options)
    yield d
    d.quit()


@pytest.fixture
def protected_driver():
    secret = os.getenv("CF_TEST_SECRET")
    assert secret, "CF_TEST_SECRET is missing"

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115 Safari/537.36")
    driver =webdriver.Chrome(options=options)

    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd(
        "Network.setExtraHTTPHeaders",
        {
            "headers": {
                "x-ci-secret": secret
            }
        }
    )

    yield driver
    driver.quit()

def test_google(driver):
    driver.get("https://google.com")
    assert "Google" in driver.title


def test_mysite(protected_driver):
    protected_driver.get("https://tarunsingh.co.in/")
    protected_driver.add_cookie({
        "name":"CF_Authorization",
        "value": os.getenv("CF_TEST_SECRET"),
        "domain": ".tarunsingh.co.in",
        "path": "/"
    })
    protected_driver.get("https://tarunsingh.co.in")

    WebDriverWait(protected_driver, 10).until(lambda d: d.title != "")
    assert "Tarun Singh" in protected_driver.title

    print("URL:", protected_driver.current_url)
    print("TITLE:", protected_driver.title)
    print("SOURCE:", protected_driver.page_source[:500])
    protected_driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    element = WebDriverWait(protected_driver, 10).until( 
        EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="https://tarunsingh.co.in/courses/"]')))
    


    protected_driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

    WebDriverWait(protected_driver, 5).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a[href="https://tarunsingh.co.in/courses/"]')
    ))
    protected_driver.execute_script("arguments[0].click();", element)


