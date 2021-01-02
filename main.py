# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep



#browser = webdriver.Firefox(executable_path=r'C:\Users\khana\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.8\geckodriver.exe')
browser = webdriver.Chrome(executable_path=r'C:\Users\khana\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.8\chromedriver.exe')

modelNo = 'EG0691.html'
browser.get('https://www.adidas.com/us/ultraboost-20-shoes/'+ modelNo)
SelectShoeSize = browser.find_element_by_css_selector('button.gl-label:nth-child(10) > span:nth-child(1)')
SelectShoeSize.click()

AddToBag = browser.find_element_by_css_selector('.add-to-bag___3wgQk > button:nth-child(1) > span:nth-child(1)')
AddToBag.click()

browser.refresh()
sleep(10)

ViewBag = browser.find_element_by_css_selector('#app > div > div > div > div > div.header___1FxHS.gl-is-sticky > div.header-mobile___4Xt19.header-refresh___1eZZF > div.right-items___1cAz5 > div > a > svg')
ViewBag.click()
sleep(3)

CheckOut = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/div/aside/div[1]/div[1]/div/div[3]/div[1]/button/span')
CheckOut.click()
sleep(3)
#Personal info textfields

#firstName
firstName = browser.find_element_by_xpath("//input[@name='firstName']")\
    .send_keys('John')

lastName = browser.find_element_by_xpath("//input[@name='lastName']")\
    .send_keys('Doe')

address1 = browser.find_element_by_xpath('//input[@name=\"address1\"]')\
    .send_keys('100 Hollywood Blvd')

city_town = browser.find_element_by_xpath('//input[@name=\"city\"]')\
    .send_keys('Los Angeles')

zipcode = browser.find_element_by_xpath("//input[@name='zipcode']")\
    .send_keys('20906')

phoneNumber = browser.find_element_by_xpath("//input[@name='phoneNumber']")\
    .send_keys('4435281001')

email = browser.find_element_by_xpath("//input[@name='emailAddress']")\
    .send_keys('khanair11@gmail.com')

#Select State
clickDropDown = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div[6]/span/div/div").click()
browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div[6]/span/div/div/select/option[25]').click()

Pay = browser.find_element_by_css_selector('#app > div > div > div > div > div.checkout_page___bUohj.delivery-page > '
                                           'div > main > div.col-m-12.col-s-12.gl-vspace-bpall-medium > button').click()

sleep(18)

#Payment method
iframeElement = browser.find_element_by_tag_name('iframe-form')
browser.switch_to.frame(iframeElement)
#WebDriverWait(browser, 20).until(EC.frame_to_be_available_and_switch_to_it(By.XPATH, "//iframe[@id = "))
cardNumber = browser.find_element_by_xpath("/html/body/form/input[1]").send_keys(4258284530541516)
CVV = browser.find_element_by_xpath('/html/body/form/input').send_keys(321)
CardExpiration = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/main/div[2]/div[1]/div[2]/div/div/div/form/div[4]/div/input")\
    .send_keys(321)

