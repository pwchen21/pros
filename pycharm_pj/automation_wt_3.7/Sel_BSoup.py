from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.momoshop.com.tw/main/Main.jsp")
driver.set_window_size(1050, 708)
driver.find_element(By.ID, "keyword").send_keys("舒潔平版")
driver.find_element(By.CSS_SELECTOR, ".inputbtn").click()
driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .prdImg").click()
#driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .swiper-slide:nth-child(1) > .prdImg").click()
prduct_url=driver.current_url
#
driver.get(prduct_url)
for x in range(1, 4):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
#print(soup)

product_name = soup.find('title')
pn = str(product_name).split('>')[1].split('<')[0]
price_price = soup.find_all('li', {'class': 'special'})
pp=str(price_price[0].find('span')).split('>')[1].split('<')[0]
print(pn, ': $', pp)


