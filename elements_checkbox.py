from selenium import webdriver
from random import choice

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get('https://demoqa.com/checkbox')

navegador.find_element_by_xpath('//*[@id="tree-node"]/ol/li/span/button').click()
lista_xpath = ['//*[@id="tree-node"]/ol/li/ol/li[1]/span/label/span[3]',
               '//*[@id="tree-node"]/ol/li/ol/li[2]/span/label/span[3]',
               '//*[@id="tree-node"]/ol/li/ol/li[3]/span/label/span[3]']
navegador.find_element_by_xpath(choice(lista_xpath)).click()
