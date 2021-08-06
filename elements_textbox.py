from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get('https://demoqa.com/text-box')

navegador.find_element_by_xpath('//*[@id="userName"]').send_keys('Vinnicius Martins')
navegador.find_element_by_xpath('//*[@id="userEmail"]').send_keys('vinnicius.o.martins@gmail.com')
navegador.find_element_by_xpath('//*[@id="currentAddress"]').send_keys('Rua Rancho Alegre, 5')
navegador.find_element_by_xpath('//*[@id="permanentAddress"]').send_keys('Santíssimo')
navegador.find_element_by_xpath('//*[@id="submit"]').send_keys(Keys.ENTER)