from selenium import webdriver
#from PIL import Image

driver = webdriver.Chrome()
driver.get('http://irs.thsrc.com.tw/IMINT/')
"""
driver.save_screenshot('test.jpg')
element = driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')
element.location
element.size
left = element.location['x']
right = element.location['x'] + element.size['width']
top = element.location['y']
bottom = element.location['y'] + element.size['height']
left, right, top, bottom
img = Image.open('test.jpg')
img = img.crop((left, top, right, bottom))
img.show()
img.save('captua.jpg', 'jpeg')
"""