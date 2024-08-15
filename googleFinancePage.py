from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



class googleFinancePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def ul_element(self):
        return self.driver.find_element(By.CLASS_NAME, "sbnBtf")
    
    def get_stock_symbols(self):
        li_elements = self.ul_element.find_elements(By.TAG_NAME, "li")
        symbols = []
        for li in li_elements:
            div_element = li.find_element(By.CLASS_NAME, "COaKTb")
            symbols.append(div_element.text)
        return symbols

