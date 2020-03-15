import time
from discobot import doit
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


if __name__ == '__main__':
    driver = webdriver.Chrome(r"C:\Users\estef\Downloads\driver\chromedriver.exe")
    try:

        driver.get('https://nackademin.learnpoint.se/')

        loginUser = driver.find_element_by_name('ctl00$MainContentPlaceHolder$ctlUserLoginControl$txtUserName')
        loginUser.send_keys('syh15s010')
        loginPass = driver.find_element_by_name('ctl00$MainContentPlaceHolder$ctlUserLoginControl$txtPassword')
        loginPass.send_keys('1Atkk5a7d1210')
        loginButton = driver.find_element_by_name('ctl00$MainContentPlaceHolder$ctlUserLoginControl$btnLogin')
        loginButton.click()

        studiePlan = driver.find_element_by_link_text('Studieplan')
        studiePlan.click()

        #At this moment the tag where windows server grade has the id ..ct105_lblMarkName
        course = 5
        while(True):
            windowsServerBetyg = driver.find_element_by_id(
                f'ctl00_MainContentPlaceHolder_ctlCoursesOfStudentControl_rptCourses_ctl0{course}_lblMarkName')
            if(windowsServerBetyg==''):
                time.sleep(3600)
                continue
            else:
                doit()
    except NoSuchElementException as e:
        driver.close()
        err = str(e)
        file1 = open("error.txt", "a")  # append mode
        file1.write(err)
        file1.close()
        doit(e)

