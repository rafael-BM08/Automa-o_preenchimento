from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver


automatico = webdriver.Chrome()

automatico.get('https://practicetestautomation.com/practice-test-login/')
sleep(2)

automatico.find_element("xpath", "//*[@id='username']").send_keys('do aluno')

automatico.find_element(
    "xpath", "//*[@id='password']").send_keys('Password123')
sleep(2)

automatico.find_element("xpath", "//*[@id='submit']").click()
sleep(3)


automatico.get(
    'https://testpages.eviltester.com/styled/basic-html-form-test.html')
sleep(2)

automatico.find_element(
    "xpath", '//*[@id="HTMLFormElements"]/table/tbody/tr[1]/td/input').send_keys('Rafael')
automatico.find_element(
    "xpath", '//*[@id="HTMLFormElements"]/table/tbody/tr[2]/td/input').send_keys('Fael1234')
automatico.find_element("xpath", '//*[@id="HTMLFormElements"]/table/tbody/tr[3]/td/textarea').send_keys(
    'Hoje acordei bem melhor que ontem de manhâ, estava doente')
automatico.find_element(
    "xpath", '//*[@id="HTMLFormElements"]/table/tbody/tr[5]/td/input[3]').click()
automatico.find_element(
    "xpath", '//*[@id="HTMLFormElements"]/table/tbody/tr[6]/td/input[1]').click()
automatico.find_element(
    "xpath", '//*[@id="HTMLFormElements"]/table/tbody/tr[7]/td/select/option[4]').click()
automatico.find_element(
    "xpath", '//*[@id="HTMLFormElements"]/table/tbody/tr[8]/td/select').click()
sleep(3)
automatico.find_element(
    "xpath", '//*[@id="HTMLFormElements"]/table/tbody/tr[9]/td/font/font/input').click()
sleep(25)
input('')
