import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
    #  driver.set_window_position(50,50)
    driver.set_window_size(1260,700)
  
    assert "Tarun Singh" in driver.title 

    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="https://tarunsingh.co.in/courses/"]')))
    


    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a[href="https://tarunsingh.co.in/courses/"]')
    ))
    driver.execute_script("arguments[0].click();", element)


