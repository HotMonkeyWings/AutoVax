from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium. common. exceptions import NoSuchElementException
from datetime import datetime
import time
from playsound import playsound
from sys import platform

# Find OS
def identifyOS():
    filePath = ''
    if platform == 'linux' or platform == 'linux2':
        filePath = './linux/geckodriver'
    elif platform == 'win32' or platform == 'win64':
        filePath = './win/geckodriver.exe'
    else:
        filePath = './macos/geckodriver'
    return webdriver.Firefox(options=fireFoxOptions, executable_path=filePath)


# Find available slots
def availabilityFinder(browser, place):
    available = browser.find_elements(By.CLASS_NAME, 'dosetotal')
    currentTime = datetime.now()
    currentTime = currentTime.strftime("%H:%M:%S")
    if len(available) > 0:
        print(str(currentTime) + ': Doses available in ' + place)

        playsound('./notif.mp3')

    else:
        print(str(currentTime) + ': No doses available in ' + place)


# Selects right district
def districtSelector(browser, state, district):
    state = int(state)
    district = int(district)
    # Selects State
    browser.find_element(By.ID, 'mat-select-0').click()
    xpath = '/html/body/div[2]/div[2]/div/div/div/mat-option[{}]/span'.format(
        state)
    browser.find_element(By.XPATH, xpath).click()

    time.sleep(0.1)

    # Selects District
    xpath = '/html/body/div[2]/div[2]/div/div/div/mat-option[{}]/span'.format(
        district)
    browser.find_element(By.ID, 'mat-select-2').click()
    browser.find_element(By.XPATH, xpath).click()


# Select by district
def searchByDistrict(fireFoxOptions):
    districts = [
        'Alapuzha',
        'Ernakulam',
        'Idukki',
        'Kannur',
        'Kasaragod',
        'Kollam',
        'Kottayam',
        'Kozhikode',
        'Malappuram',
        'Palakkad',
        'Pathanamthitta',
        'Thiruvananthapuram',
        'Thrissur',
        'Wayanad'
    ]

    print('Districts')
    print('---------')
    print('1. Alapuzha\n2. Ernakulam\n3. Idukki\n4. Kannur\n5. Kasaragod\n6. Kollam\n7. Kottayam\n8. Kozhikode\n9. Malappuram\n10. Palakkad\n11. Pathanamthitta\n12. Thiruvananthapuram\n13. Thrissur\n14. Wayanad\n')

    primary = int(input("Enter Primary District: "))
    secondary = int(input("Enter Secondary District: "))

    browser = identifyOS()
    browser.get('https://www.cowin.gov.in/')

    browser.find_elements(By.CLASS_NAME, 'mat-tab-label-content')[1].click()

    cnt = 1
    place = ''

    print()

    while 1:
        if cnt % 2 == 0:
            districtSelector(browser, 18, primary)
            place = districts[primary-1]
        else:
            districtSelector(browser, 18, secondary)
            place = districts[secondary-1]

        try:
            # Hit Search
            browser.find_element(By.CLASS_NAME, 'pin-search-btn').click()

            # Select 18+
            browser.find_element(
                By.XPATH, '/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/div[1]/label').click()

            availabilityFinder(browser, place)

        except NoSuchElementException:
            print('[!] Error! Notify MonkeyWings that he\'s a bad Programmer.')

        if cnt % 2 == 0:
            time.sleep(10)
        cnt += 1

    browser.quit()

# Search by PIN
def searchByPIN(fireFoxOptions):
    pins = input('Enter PINs (space separated): ').split()

    browser = identifyOS()
    browser.get('https://www.cowin.gov.in/')

    browser.find_elements(By.CLASS_NAME, 'mat-tab-label-content')[0].click()

    searchBar = browser.find_element(By.ID, 'mat-input-0')

    while 1:
        for pin in pins:
            searchBar.clear()
            searchBar.send_keys(pin)
            try:
                # Hit Search
                browser.find_element(By.CLASS_NAME, 'pin-search-btn').click()

                # Select 18+
                browser.find_element(
                    By.XPATH, '/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/div[1]/label').click()

                availabilityFinder(browser, pin)

            except NoSuchElementException:
                print('[!] Error! Notify MonkeyWings that he\'s a bad Programmer.')
            time.sleep(0.1)
        time.sleep(10)


if __name__ == "__main__":
    fireFoxOptions = Options()

    # GUI or Headless
    fireFoxOptions.headless = True if int(
        input('1. GUI\n2. Background\nOption: ')) == 2 else False

    print()

    opt = int(input('1. Search by PIN\n2. Search by District\nOption: '))

    print()

    if opt == 1:
        searchByPIN(fireFoxOptions)

    elif opt == 2:
        searchByDistrict(fireFoxOptions)

    else:
        pass
