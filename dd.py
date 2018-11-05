from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
time.sleep(15)
print(f'Imprimindo conteudo do Driver: {dir(driver)}')
time.sleep(20)
contato = driver.find_element_by_tag_name("input")
contato.send_keys("Vania")
time.sleep(1)
contato.send_keys(Keys.TAB)
contato.send_keys(Keys.TAB)
contato.send_keys(Keys.TAB)
time.sleep(1)
elem = driver.find_element_by_class_name("_2S1VP")
msg = 'Mensagem do e-mark'
msg2 = 'Lista de palavras:'
elem.send_keys(msg)
elem.send_keys(Keys.RETURN)
elem.send_keys(msg2)
elem.send_keys(Keys.RETURN)
a = []
for i in range(100):
    a.append(str(i)+"-oi\noi\noi\noi\noi\noi\noi\noi\noi\noi\noi\noi\noi\noi\noi\noi\noi\noi\noi\noi\n")
for gay in a:
    print(gay)
    elem.send_keys(gay)
    elem.send_keys(Keys.RETURN)

time.sleep(1)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

'''
<div class="_2S1VP copyable-text selectable-text" contenteditable="true" data-tab="1" dir="ltr" spellcheck="true">
</div>
'''

