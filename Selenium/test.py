from selenium import webdriver   
chromedriver = "D:\GitRoot\pros\selenium\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.google.com/")