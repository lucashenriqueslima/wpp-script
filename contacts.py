    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options


    browser = webdriver.Chrome()
    browser.get('https://accounts.google.com/servicelogin')
    search_form = browser.find_element_by_id("identifierId")
    search_form.send_keys('mygmail')
    nextButton = browser.find_elements_by_xpath('//*[@id ="identifierNext"]') 
    search_form.send_keys('password')
    nextButton[0].click() 