from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
	browser.switch_to.window(browser.window_handles[1])

	answer = calc(browser.find_element(By.ID, "input_value").text)

	browser.find_element(By.ID, "answer").send_keys(answer)
	browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
	#time.sleep(10)
	print(browser.switch_to.alert.text)
	browser.quit()





	
