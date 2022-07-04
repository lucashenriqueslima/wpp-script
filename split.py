from calendar import c
import os
from pickle import NONE
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

def search_for_contact(browser_instance, contact, data):
    input_seacrh = WebDriverWait(browser_instance, 1000).until(EC.element_to_be_clickable((By.CLASS_NAME, "selectable-text")))
    input_seacrh.click()
    input_seacrh.send_keys(Keys.CONTROL, "a")
    input_seacrh.send_keys(Keys.BACKSPACE)
    input_seacrh.click()
    time.sleep(2)
    input_seacrh.send_keys(contact)

    time.sleep(4)

    if browser_instance.find_elements(By.CSS_SELECTOR ,"div[style='height: 49px; width: 49px;']") :
        
        input_seacrh.send_keys(Keys.ENTER)
        print("Encontrou o contato")
        return True
    
    if len(contact.split(" ")) > 1:
        contac_next_try = contact.split(" ");
        contact = contac_next_try[0] + " " + contac_next_try[1][1:];
        input_seacrh.send_keys(Keys.CONTROL, "a")
        input_seacrh.send_keys(Keys.BACKSPACE)
        input_seacrh.click()
        time.sleep(1)
        input_seacrh.send_keys(contact) 
        time.sleep(4)
    
    if browser_instance.find_elements(By.CSS_SELECTOR ,"div[style='height: 49px; width: 49px;']"):
        input_seacrh.send_keys(Keys.ENTER)
        
        return True

    response = requests.post("https://www.studiomfotografia.com.br/api/scripts/save-regua-cobranca-erro?passwd=a)()8***0--asf", {"id_duplicata_fatura": data['id_item'], "nome_formando": data['nome_formando'], "cod_formando": data['id'], "telefone": data['telefone'], "parcela": data['parcela_atual'], "motivo": "Número não encontrado"})
    print(response.text)
    print("Contact not found")
    return False


def send_message(browser_instance, message):
    elements = browser_instance.find_elements(By.CLASS_NAME, "copyable-text")
    input_message = elements[len(elements) - 1]

    print(input_message.text)

    if(input_message.text == ""):
        input_message.send_keys(message)
        input_message.send_keys(Keys.ENTER)

def send_document(browser_instance, document_path):
    browser_instance.find_element(By.CSS_SELECTOR, ("span[data-icon='clip']")).click()
    attach = browser_instance.find_element(By.CSS_SELECTOR, "input[type='file']")
    attach.send_keys(document_path)
    time.sleep(4)
    send_button = WebDriverWait(browser_instance, 10).until(EC.element_to_be_clickable((browser_instance.find_element(By.CSS_SELECTOR, "span[data-icon='send']")))).click()        

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

datas = requests.get("https://www.studiomfotografia.com.br/api/scripts/get-regua-cobranca-to-script?passwd=a)()8***0--asf").json()
base_dir = "C:\\Users\\Studio M\\Documents\\"

# for data in datas:

#     url_to_get_pdf = data['boleto_wpp']

#     response = requests.get(url_to_get_pdf)

    

#     if response.status_code == 200:
#         file_path = os.path.join(base_dir, f"{data['id_item']}.{'html' if data['link'] != None else 'pdf'}")
#         with open(file_path, "wb") as f:
#             f.write(response.content)

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir={}".format(profile))

servico =  Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico, chrome_options=options)

base_dir = "C:\\Users\\Studio M\\Documents\\"

browser.get("https://web.whatsapp.com/")
input_seacrh = WebDriverWait(browser, 1000).until(EC.element_to_be_clickable((By.CLASS_NAME, "selectable-text")))
input_seacrh.click()
time.sleep(2)
input_seacrh.send_keys("teste")
for data in datas:
    if(search_for_contact(browser, data['telefone'], data) == True):
        time.sleep(2)
        send_message(browser, data['mensagem_wpp'])
        send_document(browser, base_dir + data['id_item'] + f".{'html' if data['link'] != None else 'pdf'}")
time.sleep(1000)


