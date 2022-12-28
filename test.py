from selenium import webdriver
from selenium.webdriver import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path= "C:\Program Files (x86)\chormedriver.exe")

driver.get("https://www.pingodoce.pt/")

driver.maximize_window()


#time.sleep(3)

#noti = driver.find_element(by=By.CLASS_NAME, value='deny')
#noti.click()



time.sleep(5)

cooki = driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
cooki.click()

time.sleep(5)



elem = driver.find_element(by=By.NAME, value="s")
elem.clear()
elem.send_keys("Receitas de Panquecas")
elem.send_keys(Keys.RETURN)

time.sleep(5)

pan = driver.find_elements(by=By.CLASS_NAME, value='title')



for x in pan:
    q = x.text.count("panquecas")  
    p = x.text.count("Panquecas")    
   
print(q+p)


 