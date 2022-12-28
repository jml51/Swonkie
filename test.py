from selenium import webdriver
from selenium.webdriver import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path= "C:\Program Files (x86)\chormedriver.exe")

driver.get("https://www.pingodoce.pt/")

driver.maximize_window()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "webPushSolicitation"))
    )

    noti = driver.find_element(by=By.XPATH, value="html/body/div[1]/div[1]/div[4]/div/button[1]")
    noti.click()

finally:
    driver.quit()



time.sleep(5)

cooki = driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
cooki.click()

time.sleep(5)



elem = driver.find_element(by=By.NAME, value="s")
elem.clear()
elem.send_keys("Receitas de Panquecas")
elem.send_keys(Keys.RETURN)


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
    )

    #pan = driver.find_elements(by=By.PARTIAL_LINK_TEXT, value="Panquecas")
    #print(pan)
finally:
    driver.quit()




#pan = driver.find_element(by=By.XPATH, value="")
 