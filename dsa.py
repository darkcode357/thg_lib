from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#abre o chrome
driver = webdriver.Chrome()


#faz request na pg
for i in range(1, 780):
    driver.get("http://www.allitebooks.com/page/%s/" %str(i))
    try:
        for handlers in driver.window_handles:
            if driver.window_handles == 2:
                driver.switch_to.window(handlers)
            else:
                i = 0
                while  i >= 10:
                    if driver.find_elements_by_tag_name("article") == None:
                        break
                    options = driver.find_elements_by_tag_name("article")
                    div = options[i].find_elements_by_tag_name("div")
                    aref = div[1].find_element_by_tag_name("a")
                    aref.click()
                    elemente_pub = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "download-links")))
                    btnDownload = driver.find_elements_by_class_name("download-links")
                    saida = btnDownload[0].click()
                    i = i+1
                    driver.back()

    finally:
        driver.quit()
