from appium import webdriver

desire_caps= {
    "deviceName" : "Android Emulator", 
    "automationNmame" : "appium",
    "platformName" : "Android",
    "platformVersion" : "7.0",
    "appPackage" : "com.android.calculator2",
    "appActivity": ".Calculator"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_caps)

driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_2").click()
driver.find_element_by_id("com.android.calculator2:id/digit_eq").click()

driver.quit()

