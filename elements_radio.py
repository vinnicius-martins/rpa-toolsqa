from selenium import webdriver
from random import choice

navegador = webdriver.Chrome()
navegador.get('https://demoqa.com/radio-button')
xpaths = ['//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/label',
          '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/label']
navegador.find_element_by_xpath(choice(xpaths)).click()