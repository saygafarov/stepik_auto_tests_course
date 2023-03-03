from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


try:
	link = "https://suninjuly.github.io/selects2.html"
	brouser = webdriver.Chrome()
	brouser.get(link)

	num1 = brouser.find_element(By.ID, "num1")
	num2 = brouser.find_element(By.ID, "num2")
	print(num1.text)
	print(num2.text)

	answer = int(num1.text) + int(num2.text)
	print(answer)

	select = Select(brouser.find_element(By.TAG_NAME, "select"))
	select.select_by_value(str(answer))

	brouser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
	

finally:
	time.sleep(30)
	brouser.quit()



