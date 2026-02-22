import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def test_addition():
    assert 2 + 3 == 5

def test_one():
    assert 5 > 1

def test_two():
    assert 3 * 2 == 6

@pytest.fixture

def driver():
    driver =webdriver.Chrome()
    yield driver
    driver.quit()

def test_google(driver):
    driver.get("https://google.com")
    assert "Google" in driver.title


def test_mysite(driver):
    driver.get("https://tarunsingh.co.in")
    WebDriverWait(driver, 10).until(lambda d: d.title !="")
    assert "Tarun Singh" in driver.title 