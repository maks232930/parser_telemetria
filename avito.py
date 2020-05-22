from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.avito.ru/moskva/predlozheniya_uslug/remont_noutbukov.kompyuternyy_master.chestnye_tseny_1928562539")
btn_cookie = driver.find_element_by_class_name('item-phone')
btn_cookie.click()
btn_number = driver.find_element_by_class_name('item-phone-big-number')
print(btn_number)
print(btn_number.get_attribute('src'))
# btn_run = driver.find_element_by_class_name('start-text')
# btn_run.click()
# ip = driver.f('result-data')
# print(ip.text)