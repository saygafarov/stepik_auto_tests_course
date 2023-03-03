from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	
	button = browser.find_element(By.TAG_NAME, "button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()

	answer = calc(browser.find_element(By.ID, "input_value").text)


	browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(answer)
	browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
	browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
	browser.find_element(By.TAG_NAME, "button").click()
	
	

finally:
	time.sleep(10)
	browser.quit()




	
