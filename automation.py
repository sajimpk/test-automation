from selenium import webdriver
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("https://www.google.com")
element_search_box = driver.find_element(By.NAME, "q").send_keys("Start")
driver.find_element(By.NAME, "q").submit()

find = driver.find_element(By.NAME, "q").clear()

driver.find_element(By.NAME, "q").send_keys('canada')
time.sleep(5)

s = [driver.find_element(By.XPATH, "//*[@id='Alh6id']/div[1]/div/ul")]

# create list all of data
li=[]
lt=[]
for i in s:
    t = i.text
    li.append(t)
    li=str(t)
    a = li.splitlines()
    lt.append(a)


# largest  data 
fs = 0
lis =[]
for j in lt:
    for y in j:
        l = len(y)
        print(f'{y}')
        if fs < l :
            lis.clear()
            lis.append(y)
            print(f' its < {y}')
            fs = l
        elif fs == l:
            lis.append(y)
            print(f' its == {y}')
            fs = l
print(lis)

# lowest data  found 

fs1 = fs
lis1 =[]
for j in lt:
    for y in j:
        l = len(y)
        print(f'{y}')
        if fs1 > l :
            lis1.clear()
            lis1.append(y)
            print(f' its < {y}')
            fs1 = l
        elif fs1 == l:
            lis1.append(y)
            print(f' its == {y}')
            fs1 = l
print(lis1)
time.sleep(3)

print(f'the largest data is : {lis}')
print(f'the lowest data is : {lis1}')


