import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

def search_for_contact(browser_instance, contact):
    input_seacrh = WebDriverWait(browser_instance, 1000).until(EC.element_to_be_clickable((By.CLASS_NAME, "selectable-text")))
    input_seacrh.send_keys(Keys.CONTROL, "a")
    input_seacrh.send_keys(Keys.BACKSPACE)
    input_seacrh.send_keys(contact)
    time.sleep(1)
    input_seacrh.send_keys(Keys.ENTER)

def send_message(browser_instance, message):
    elements = browser_instance.find_elements(By.CLASS_NAME, "copyable-text")
    input_message = elements[len(elements) - 1]
    input_message.send_keys(message)
    input_message.send_keys(Keys.ENTER)

def send_document(browser_instance, document_path):
    browser_instance.find_element(By.CSS_SELECTOR, ("span[data-icon='clip']")).click()
    attach = browser_instance.find_element_by_css_selector("input[type='file']")
    attach.send_keys(document_path)
    time.sleep(2)
    WebDriverWait(browser_instance, 10).until(EC.element_to_be_clickable((browser_instance.find_element_by_css_selector("span[data-icon='send']")))).click()        

def select_contact_area_for_scrap():
    contact_area = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/div[3]')
    contact_area.send_keys(Keys.CONTROL + Keys.HOME).send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(1)

def send_to_contact(contact, message, need_to_send_document, document_path):
    search_for_contact(browser, contact)
    send_message(browser, message)
    if(need_to_send_document):
        send_document(browser, document_path)   


def do_scrap_function(contact, message, need_to_send_document, document_path):
    select_contact_area_for_scrap()
    

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir={}".format(profile))

servico =  Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico, chrome_options=options)

browser.get("https://web.whatsapp.com/")

grps = ["Goianins"]

for grp in grps:
    print("Searching for group: " + grp)
    search_for_contact(browser, grp)

    time.sleep(2)

    menssages = browser.find_elements(By.CLASS_NAME, "focusable-list-item")

    print(menssages)

    menssages.pop(1);

    for message in menssages:
        try:
            
            date = message.find_element(By.CLASS_NAME, "copyable-text").get_attribute("data-pre-plain-text")
            date_to_compare = date.split(",")[1].split("]")[0].replace(" ", "").replace("]", "")
            
            if(date_to_compare != datetime.today().strftime('%d/%m/%Y')):
                continue
            
            print(message.find_element(By.CLASS_NAME, "selectable-text"))
            message.click()

            time.sleep(3)
            break

            # message_found = message.find_element(By.CLASS_NAME, "selectable-text").text
            # print(date + " " + message_found)
        except (NoSuchElementException) as e:
            None













