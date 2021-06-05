from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import time
from playsound import playsound

def placeSelector(browser, state, district):
    state = int(state)
    district = int(district)
    # Selects State
    browser.find_element(By.ID,'mat-select-0').click()
    xpath = '/html/body/div[2]/div[2]/div/div/div/mat-option[{}]/span'.format(state)
    browser.find_element(By.XPATH,xpath).click()

    time.sleep(0.1)

    # Selects District
    xpath = '/html/body/div[2]/div[2]/div/div/div/mat-option[{}]/span'.format(district)
    browser.find_element(By.ID,'mat-select-2').click()
    browser.find_element(By.XPATH, xpath).click()

    # 1 - Alapuzha
    # 2 - Ernakulam
    # 5 - Kasargod

if __name__=='__main__':

    fireFoxOptions = Options()
    fireFoxOptions.headless = True
    browser = webdriver.Firefox(options=fireFoxOptions,executable_path='./geckodriver')
    browser.get('https://www.cowin.gov.in/')
    cnt = 1
    browser.find_elements(By.CLASS_NAME, 'mat-tab-label-content')[-1].click()
    while 1:
        place = ''
        if cnt%2 == 0:
            placeSelector(browser, 18, 2)
            place = "Ernakulam"
        else:
            placeSelector(browser, 18, 1)
            place = "Alapuzha"

        # Hit Search
        browser.find_element(By.CLASS_NAME,'pin-search-btn').click()

        # Select 18+
        browser.find_element(By.XPATH,'/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/div[1]/label').click()

        # Availabe slots have a 'dosetotal' class name (Although it could glitch beyond 100+ due to number of entries per second)
        available = browser.find_elements(By.CLASS_NAME,'dosetotal')

        currentTime = datetime.now()
        currentTime = currentTime.strftime("%H:%M:%S")
        if len(available) > 0:
            print(str(currentTime) + ": Doses available in " + place)
            playsound('./notif.mp3')
        else:
            print(str(currentTime) + ": No doses available in " + place)

        if cnt%2 == 0:
            time.sleep(10)
        cnt += 1
    browser.quit()
