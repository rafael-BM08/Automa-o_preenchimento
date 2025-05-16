from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import os


varrer = webdriver.Chrome()

# 1 - entrar no site https://practicetestautomation.com/practice-test-login/

varrer.get('https://practicetestautomation.com/practice-test-login/')
sleep(3)

# 2 preencher user -//*[@id="username"] student
campo_user = varrer.find_element(
    By.XPATH, '//*[@id="username"]').send_keys('student')

# 3 preencher senha - //*[@id="password"] Password123
campo_senha = varrer.find_element(
    By.XPATH, '//*[@id="password"]').send_keys('Password123')
sleep(2)

# 4 botão - //*[@id="submit"]
bnt = varrer.find_element(By.XPATH, '//*[@id="submit"]').click()
sleep(3)

# 5 entrar site - https://clone-olx-devaprender.netlify.app/
varrer.get('https://clone-olx-devaprender.netlify.app/')
sleep(3)

# 6 pegar nome - //h3[@class="text-base text-gray-900 line-clamp-2 mb-1 hover:text-[#6E0AD6]"]
produtos = varrer.find_elements(
    By.XPATH, '//h3[@class="text-base text-gray-900 line-clamp-2 mb-1 hover:text-[#6E0AD6]"]')

# 7 - pegar preco - //span[@class="text-2xl font-bold text-gray-900"]
precos = varrer.find_elements(
    By.XPATH, '//span[@class="text-2xl font-bold text-gray-900"]')


for produto, preco in zip(produtos, precos):
    try:
        valor_str = preco.text.replace("R$", "").replace(
            ".", "").replace(",", ".").strip()
        valor_float = float(valor_str)
        if valor_float > 8000:
            with open('produtos.csv', 'a', encoding='utf-8') as arq:
                arq.write(f'{produto.text} - {preco.text}{os.linesep}')
    except Exception as e:
        print("Erro:", e)
        continue
