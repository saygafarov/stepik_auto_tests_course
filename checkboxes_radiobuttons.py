from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "https://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)

	#x_elem = brouser.find_element(By.CSS_SELECTOR, "#input_value")
	answer = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)

	browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(answer)
	#input_answer.send_keys(answer)

	browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
	#checkbox.click()

	browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
	#radiobutton.click()

	browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
	#button_submit.click()

finally:
	time.sleep(30)
	browser.quit()




	
