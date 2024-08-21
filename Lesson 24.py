from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')  
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=service, options=options)

try:
    
    driver.get("https://www.gismeteo.kz/weather-astana-5164/10-days/")

    
    time.sleep(5)  

    temperature_elements = driver.find_elements(By.CLASS_NAME, 'unit_temperature_c')
    temperatures = [element.text for element in temperature_elements]
    
    print("Температуры на ближайшие 10 дней:")
    for temp in temperatures:
        print(temp)

finally:
    driver.quit()