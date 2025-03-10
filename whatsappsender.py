# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 19:01:19 2025

@author: conta
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
import os


class WhatsappSender:
    def __init__(self):
        super().__init__()
        self.options = Options()
        self.pathToUserData='./UserDataProfile'
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        self.driver = None
        self.firstRun = False

    def initialize(self, firstRun=False, pathToUserData='', userAgent='', pathToBrowser=''):
        """

        :param firstRun: bool Set to True the first time to log in to your whatsapp account
        :param pathToUserData: string You can specify your user data browser folder (Profile)
        :param userAgent: string You can use a specific user agent
        :param pathToBrowser string You can specify where to find you preferred browser
        :return:
        """
        try:
            self.firstRun = firstRun
            if pathToUserData:
                self.pathToUserData = pathToUserData
            if not os.path.exists(self.pathToUserData):
                # Create if folder does not exist
                os.makedirs(self.pathToUserData)
                print(f"Folder '{os.path.abspath(self.pathToUserData)}' created.")
            self.options.add_argument(f"user-data-dir={os.path.abspath(self.pathToUserData)}")
            if userAgent:
                self.userAgent = userAgent
            if pathToBrowser:
                self.options.binary_location = pathToBrowser
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--window-size=1920,1080')
            self.options.add_argument("--no-first-run")
            self.options.add_argument("--no-default-browser-check")
            self.options.add_argument(f'user-agent={self.userAgent}')
            if not self.firstRun:
                self.options.add_argument('--headless=new')  # Utilise le mode headless
            self.driver = webdriver.Chrome(options=self.options)
            if self.firstRun:
                address = f"https://web.whatsapp.com/"
                self.driver.get(address)
                try :
                    WebDriverWait(self.driver, 60).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "[contenteditable='true']"))
                    )
                    print("Successfully authenticated, browser will close, you can set firstRun to False to use sendWhatsappMessage")
                except Exception as e:
                    print("Error authenticating", e)
                finally:
                    time.sleep(5)
                    self.driver.quit()
                    sys.exit(0)
        except Exception as e:
            if self.driver:
                self.driver.quit()
            raise (Exception("e"))

    def sendWhatsappMessage(self, phone_number, message):
        """

        :param phone_number: in international format +XX X XX XX XX XX
        :param message:
        :return:
        """

        try:
            # access WhatsApp Web
            address = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"
            self.driver.get(address)

            # waiting page is loaded (max 60s)
            try:
                WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[contenteditable='true']"))
                )
                time.sleep(1)
                try:
                    # Click on send
                    send_button = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Envoyer')]")
                    send_button.click()
                    time.sleep(1)
                except:
                    self.driver.quit()
                    raise (Exception('Send button not found'))
            except:
                self.driver.quit()
                raise (Exception("Timeout : page did not load correctly."))

            # END
            self.driver.quit()
            return 0
        except Exception as e:
            if self.driver:
                self.driver.quit()
            raise (Exception("e"))


