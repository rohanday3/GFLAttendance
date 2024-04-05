#!/usr/bin/env python3

'''
    Author: Rohan Dayaram
    Date: 2024-03-05
    Description: This is a simple script to fill out a form on a website using selenium
    https://github.com/rohanday3/GFLAttendance
    Version: 1.0
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import datetime

from time import sleep
from json import *

chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_service = ChromeService("/usr/lib/chromium-browser/chromedriver")

class FormFiller:
    def __init__(self,data):
        self.data = data
        display = Display(visible=0, size=(800, 600))
        display.start()
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

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
            modules_path = '//*[@id="question-list"]/div[4]/div[2]/div/div/div'
            modules = questions.find_elements(By.XPATH, modules_path)
            for module in modules:
                module_name = module.find_element(By.XPATH, 'div/label/span[2]')
                print(module_name.text)
                if module_name.text == self.data["module"]:
                    module.click()
                    break
            submit = questions.find_element(By.XPATH, '//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button')
            submit.click()
            self.driver.quit()

if __name__ == "__main__":
    with open("login.json", "r") as file:
        data = load(file)
    form = FormFiller(data)
    form.fill_form()
