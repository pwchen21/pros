from selenium import webdriver

driver = webdriver.Chrome('D:\GitRoot\pros\Selenium\chromedriver\chromedriver_win32_104\chromedriver.exe')
driver.get("https://www.google.com.tw/")
driver.find_element_by_name("q").send_keys("test")
driver.find_element_by_name("btnK").click()
driver.quit()