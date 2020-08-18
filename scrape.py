import os
import time
from discobot import doit
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def find_ungraded_course(driver):
    #finds first empty grade
    for id in range(15):
        if driver.find_element_by_id(f'ctl00_MainContentPlaceHolder_ctlCoursesOfStudentControl_rptCourses_ctl{id:02d}_lblMarkName').text =="":
            with open("grade_id", "w") as file:
                file.write(str(id))
                file.close
            break
        

def announce_grade(driver):
    #checks if current empty grade(based on grade_id) is not empty
    #If not empty, find next empty grade and announce that course is graded
    with open("grade_id", "r") as file:
        id = file.readline()
        if driver.find_element_by_id\
            (f'ctl00_MainContentPlaceHolder_ctlCoursesOfStudentControl_rptCourses_ctl{int(id):02d}_lblMarkName').text !="":
            find_ungraded_course(driver)
            driver.quit()
            doit()
        else:
            driver.close()

def click_studieplan(driver):
    #Clicks on hamburgermenu Studieplan
    studiePlan = driver.find_element_by_link_text('Studieplan')
    studiePlan.click()

def click_login(driver):
    #Clicks on login
    loginButton = driver.find_element_by_name('ctl00$MainContentPlaceHolder$ctlUserLoginControl$btnLogin')
    loginButton.click()

def login_user(driver):
    #Enters credentials
    loginUser = driver.find_element_by_name('ctl00$MainContentPlaceHolder$ctlUserLoginControl$txtUserName')
    loginUser.send_keys('username')
    loginPass = driver.find_element_by_name('ctl00$MainContentPlaceHolder$ctlUserLoginControl$txtPassword')
    loginPass.send_keys('password')

def get_url(driver):
    driver.get('https://nackademin.learnpoint.se/')
    return driver

def scrape():
    #Surfs to studentportalen
    driver = webdriver.Chrome()
    return driver

if __name__ == '__main__':
    driver = scrape()
    get_url(driver)
    login_user(driver)
    click_login(driver)
    click_studieplan(driver)
    announce_grade(driver)

    #driver = webdriver.Chrome(r'C:\Users\estef\Downloads\driver\chromedriver.exe')
   
