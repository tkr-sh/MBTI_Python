from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from FR_questions_mbti import question_about_mbti as CF

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.reverso.net/traduction-texte")

time.sleep(5)

# Première page
ck = driver.find_element(By.ID,"didomi-notice-agree-button")
ck.click()
time.sleep(1)

for i,e in enumerate(driver.find_elements(By.CLASS_NAME,"selected-language")):
    if i == 1:
        e.click()
        time.sleep(0.5)
        for j,f in enumerate(driver.find_elements(By.CLASS_NAME,"options-item")):
            if j==len(driver.find_elements(By.CLASS_NAME,"options-item"))-6:
                f.click()
        break


for i,e in enumerate(driver.find_elements(By.CLASS_NAME,"translation-input")):
    if i == 0:
        input_us  = e
    else:
        output = e
input_us = driver.find_element(By.TAG_NAME,"textarea")

f = open("SW_questions_mbti.py","w", encoding = "utf-8" )
f.write("question_about_mbti = {\n")
list_letters = "TFSN"
letter = 'T'
choi = [["Ti","Te"],["Fi","Fe"],["Si","Se"],["Ni","Ne"]]

for i in range(80):
    french_sentence = CF["TFSN"[i//20]][str((1+(i%20//2)))][choi[(i)//20][i%2]]
    input_us.clear()
    input_us.send_keys(french_sentence)

    time.sleep(10)
    other_sentence = output.get_attribute('textContent')


    if i%20 == 0:
        letter = list_letters[i//20]

        # Write the letter
        if i != 0:
            f.write("\t},\n")
        f.write("\t'"+letter+"' : {\n")


    # Begin if i%2 == 0
    if i%2 == 0:
        f.write("\t\t'"+ str(1 +(i%20)//2)+"' : {\n")   


    line ="\t\t\t'"+letter+'ie'[i%2]+"' : \""+ other_sentence +"\""+", "[i%2]
    f.write(line+"\n")

    # End if i%2 == 1
    if i%2 == 1:
        f.write("\t\t},\n")   


f.write("\t}\n}")
