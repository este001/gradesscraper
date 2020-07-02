import os
import time
from discobot import doit
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


"""
It has to find course without grade, and announce latest course grade.
Then save current empty course grade
If course grade is != empty, repeat.
Save current id in txtfile?
"""



def course_grade():


    pass


def login_user(driver):
    #Enters credentials
    print(driver)
    loginUser = driver.find_element_by_name('ctl00$MainContentPlaceHolder$ctlUserLoginControl$txtUserName')
    loginUser.send_keys('syh15s010')
    loginPass = driver.find_element_by_name('ctl00$MainContentPlaceHolder$ctlUserLoginControl$txtPassword')
    loginPass.send_keys('Atkk5a7d1210')

def click_login(driver):
    #Clicks on login
    loginButton = driver.find_element_by_name('ctl00$MainContentPlaceHolder$ctlUserLoginControl$btnLogin')
    loginButton.click()


def click_studieplan(driver):
    #Clicks on hamburgermenu Studieplan
    studiePlan = driver.find_element_by_link_text('Studieplan')
    studiePlan.click()

def scrape():
    #Surfs to studentportalen
    driver = webdriver.Chrome()
    return driver.get('https://nackademin.learnpoint.se/')

if __name__ == '__main__':
    driver = scrape()
    login_user(driver)
    click_login(driver)
    click_studieplan(driver)
    #driver = webdriver.Chrome(r'C:\Users\estef\Downloads\driver\chromedriver.exe')
    #windowsServerBetyg = driver.find_element_by_id(f'ctl00_MainContentPlaceHolder_ctlCoursesOfStudentControl_rptCourses_ctl0{course}_lblMarkName')
