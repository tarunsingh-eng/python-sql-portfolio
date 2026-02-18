import pytest
from selenium import webdriver

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
