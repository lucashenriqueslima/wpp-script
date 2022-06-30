import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def search_for_contact(browser_instance, contact):
    input_seacrh = WebDriverWait(browser_instance, 1000).until(EC.element_to_be_clickable((By.CLASS_NAME, "selectable-text")))
    input_seacrh.send_keys(Keys.CONTROL, "a")
    input_seacrh.send_keys(Keys.BACKSPACE)
    input_seacrh.send_keys(contact)
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
    time.sleep(1)
    WebDriverWait(browser_instance, 10).until(EC.element_to_be_clickable((browser_instance.find_element_by_css_selector("span[data-icon='send']")))).click()        

def select_contact_area_for_scrap():
    contact_area = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/div[3]')
    contact_area.send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(1)
    contact_area.send_keys(Keys.CONTROL + Keys.END)

def send_to_contact(contact, message, need_to_send_document, document_path):
    search_for_contact(browser, contact)
    send_message(browser, message)
    if(need_to_send_document):
        send_document(browser, document_path)   

def do_scrap(contact, message, need_to_send_document, document_path):
    select_contact_area_for_scrap()

# datas = requests.get("https://www.studiomfotografia.com.br/teste/api/scripts/get-regua-cobranca-to-script?passwd=a)()8***0--asf").json()
# base_dir = "C:\\Users\\Studio M\\Documents\\"

# for data in datas:

#     if data['link'] != "":

#         url_to_get_pdf = f"https://api-homologacao.getnet.com.br{data['link']}"

#         response = requests.get(url_to_get_pdf)

#         if response.status_code == 200:
#             file_path = os.path.join(base_dir, f"{data['id_item']}.html")
#             with open(file_path, "wb") as f:
#                 f.write(response.content)

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir={}".format(profile))

servico =  Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico, chrome_options=options)

browser.get("https://web.whatsapp.com/")

# for data in datas:
#     search_for_contact(browser, "8599439-0988")
#     send_message(browser, "Mensagem de teste")
#     send_document(browser, "C:\\Users\\Studio M\\Documents\\imagemteste.png")
#     time.sleep(10000)









