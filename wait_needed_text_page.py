from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
	button_book = browser.find_element(By.ID, "book").click()
	

	answer = calc(browser.find_element(By.ID, "input_value").text)

	browser.find_element(By.ID, "answer").send_keys(answer)
	browser.find_element(By.ID, "solve").click()

finally:
	#time.sleep(10)
	print(browser.switch_to.alert.text)
	browser.quit()





	
