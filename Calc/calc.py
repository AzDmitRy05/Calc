import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Запуск браузера в фоновом режиме
    driver = webdriver.Chrome(options=options)
    driver.get("http://127.0.0.1:5001")
    yield driver
    driver.quit()

@pytest.mark.parametrize("num1, num2, operation, expected", [
    ("5", "3", "+", "8.0"),
    ("10", "2", "-", "8.0"),
    ("4", "3", "*", "12.0"),
    ("8", "2", "/", "4.0"),
    ("2", "3", "**", "8.0"),
    ("5", "3", "max", "5.0"),
    ("5", "3", "min", "3.0"),
    ("5", "0", "/", "Ошибка: Деление на ноль"),
    ("abc", "3", "+", "Ошибка: Введите корректные числа")
])
def test_calculator_operations(driver, num1, num2, operation, expected):
    num1_field = driver.find_element(By.NAME, "num1")
    num2_field = driver.find_element(By.NAME, "num2")
    operation_select = Select(driver.find_element(By.NAME, "operation"))
    submit_button = driver.find_element(By.TAG_NAME, "button")

    num1_field.clear()
    num1_field.send_keys(num1)
    num2_field.clear()
    num2_field.send_keys(num2)
    operation_select.select_by_value(operation)
    submit_button.click()

    time.sleep(1)

    result_text = driver.find_element(By.TAG_NAME, "h3").text
    assert expected in result_text
