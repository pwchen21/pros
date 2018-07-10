from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'D:\Download\IEDriverServer_x64_3.13.0')  # PhantomJs
driver.get('http://pala.tw/js-example/')  # 輸入範例網址，交給瀏覽器 
pageSource = driver.page_source  # 取得網頁原始碼
#print(pageSource)

#driver.close()