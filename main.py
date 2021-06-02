from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

fireFoxOptions = Options()
fireFoxOptions.headless = True
browser = webdriver.Firefox(options=fireFoxOptions,executable_path='./geckodriver')

browser.get('https://www.cowin.gov.in/home')
browser.find_elements(By.CLASS_NAME, 'mat-tab-label-content')[-1].click()

# Selects State
browser.find_element(By.ID,'mat-select-0').click()
browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/mat-option[18]/span').click()

time.sleep(0.1)

# Selects District
browser.find_element(By.ID,'mat-select-2').click()
browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/mat-option[2]/span').click()

# 1 - Alapuzha
# 2 - Ernakulam
# 5 - Kasargod

browser.find_element(By.XPATH,'/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/div/mat-tab-body[3]/div/div/div[3]/button').click()
browser.find_element(By.XPATH,'/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/div[1]/label').click()

available = browser.find_elements(By.CLASS_NAME,'dosetotal')
if len(available) > 0:
    print("Doses available")
else:
    print("No doses available")

# browser.quit()