from selenium import webdriver
from selenium.webdriver.common.by import By

brouser = webdriver.Chrome()
brouser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = brouser.find_element(By.ID, "submit_button")
