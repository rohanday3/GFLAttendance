'''
    Author: Rohan Dayaram
    Date: 2024-03-05
    Description: This is a simple script to fill out a form on a website using selenium
    https://github.com/rohanday3/GFLRegistration
    Version: 1.0
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.firefox.options
from selenium.webdriver.firefox.service import Service
import datetime

from time import sleep
from json import *

class FormFiller:
    def __init__(self,data):
        self.data = data
        # import the file firefox geckodriver
        options = selenium.webdriver.firefox.options.Options()
        options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
        gecko_path = "C:/Program Files/Mozilla Firefox/geckodriver.exe"
        service = Service(gecko_path)
        self.driver = webdriver.Firefox(options=options, service=service)

    # get the form site
    def get_form(self):
        self.driver.get(self.data["url"])
        try:
            form = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "question-list"))
            )
            return form
        except:
            print("Form not found")
            return None
        
        # fill the form
    def fill_form(self):
        form = self.get_form()
        if form:
            questions = form.find_element(By.XPATH, '//*[@id="question-list"]')
            if not questions:
                print("No questions found")
                return
            name = questions.find_element(By.XPATH, '//*[@id="question-list"]/div[1]/div[2]/div/span/input')
            name.send_keys(self.data["name"])
            email = questions.find_element(By.XPATH, '//*[@id="question-list"]/div[2]/div[2]/div/span/input')
            email.send_keys(self.data["email"])
            date = questions.find_element(By.XPATH, '//*[@id="DatePicker0-label"]')
            # M/d/yyyy
            date.send_keys(datetime.datetime.now().strftime("%m/%d/%Y"))
            module = questions.find_element(By.XPATH, '//*[@id="question-list"]/div[4]/div[2]/div/div/div[2]')
            module.click()
            submit = questions.find_element(By.XPATH, '//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button')
            submit.click()

if __name__ == "__main__":
    with open("login.json", "r") as file:
        data = load(file)
    form = FormFiller(data)
    form.fill_form()
    