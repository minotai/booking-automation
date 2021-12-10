from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound
from datetime import timedelta, datetime

driver = webdriver.Chrome()
driver.get('https://bmvs.onlineappointmentscheduling.net.au/oasis/Search.aspx')


hapi = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtHAPID"]')
hapi.send_keys('00000000')  # your HAPI id here

firstName = driver.find_element(
    By.XPATH, '//*[@id="ContentPlaceHolder1_txtFirstName"]')
firstName.send_keys('John')  # your first name

lastName = driver.find_element(
    By.XPATH, '//*[@id="ContentPlaceHolder1_txtSurname"]')
lastName.send_keys('Doe')  # your last name

dob = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtDOB"]')
dob.send_keys('01/01/1990')  # your DOB

searchButton = driver.find_element(
    By.XPATH, '//*[@id="ContentPlaceHolder1_btnSearch"]')
searchButton.click()

currentTimeRaw = driver.find_element(
    By.XPATH, '//*[@id="ContentPlaceHolder1_divAppointmentResults"]/div/div[1]/div[1]/div[2]').get_attribute('innerHTML').strip()
currentTime = datetime.strptime(currentTimeRaw, '%A, %d %B %Y @ %I:%M %p')
print(">>> current time " + currentTime.strftime('%d/%m/%Y'))

newTime = currentTime + timedelta(days=1) # start the new time with current date + 1

modifyDateButton = driver.find_element(
    By.XPATH, '//*[@id="ContentPlaceHolder1_repAppointments_lnkChangeAppointment_0"]')
modifyDateButton.click()

# Please fill these with the center names and their ids 
# You can inpect the radio button to view the id attribute (e.g. rbLocation1) 
centersDict = {
    '168': 'Sydney',
    '166': 'Bondi',
    '60': 'Paramatta'
}
currentTime = 1
newTime = 2
while newTime > currentTime:
    for key, value in centersDict.items():
        postcode = driver.find_element(
            By.XPATH, '//*[@id="ContentPlaceHolder1_SelectLocation1_txtSuburb"]')
        postcode.send_keys('2000')

        searchAreaButton = driver.find_element(
            By.XPATH, '//*[@id="form1"]/div[3]/div[2]/div/div[2]/div[5]/div[3]/input')
        searchAreaButton.click()

        bupaCenter = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located(
                (By.ID, "rbLocation" + key))
        )

        bupaCenter.click()

        if value == 'Bondi' or value == 'Paramatta': # Please modify these lines if that center need to accept the alert to proceed
            print(value)
            WebDriverWait(driver, 50).until(EC.alert_is_present())
            driver.switch_to.alert.accept()

        nextButton = driver.find_element(
            By.XPATH, '//*[@id="ContentPlaceHolder1_btnCont"]')
        nextButton.click()

        newTimeRaw = driver.find_element(
            By.XPATH, '//*[@id="ContentPlaceHolder1_SelectTime1_txtAppDate"]').get_attribute('value').strip()
        if newTimeRaw:
            newTime = datetime.strptime(newTimeRaw, '%d/%m/%Y')
        else:
            newTime = currentTime + timedelta(days=1)

        print("<<< new time " + newTime.strftime('%d/%m/%Y') + " " + value)
        if newTime > currentTime: # if the updated new time is not an ealier date, return to the previous page
            print("😭")
            backButton = driver.find_elements(By.CLASS_NAME, 'blue-button')[1]
            backButton.click()
playsound('bell.wav')
print("🎉 🎉 🎉")
