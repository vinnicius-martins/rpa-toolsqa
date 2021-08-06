from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get('https://demoqa.com/webtables')
navegador.maximize_window()

navegador.find_element_by_xpath('//*[@id="addNewRecordButton"]').click()
navegador.find_element_by_xpath('//*[@id="firstName"]').send_keys('Vinnicius')
navegador.find_element_by_xpath('//*[@id="lastName"]').send_keys('Martins')
navegador.find_element_by_xpath('//*[@id="userEmail"]').send_keys('vinnicius.o.martins@gmail.com')
navegador.find_element_by_xpath('//*[@id="age"]').send_keys('20')
navegador.find_element_by_xpath('//*[@id="salary"]').send_keys('100000000')
navegador.find_element_by_xpath('//*[@id="department"]').send_keys('Domingues e Pinho Contadores')
navegador.find_element_by_xpath('//*[@id="submit"]').click()

