from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://1cm.vn/")
assert "OneClickMoney - Bạn có thể nhận được một khoản vay lên đến 10 triệu VND online" in driver.title

#Register Page
fullname = driver.find_element_by_name("full_name")
fullname.send_keys("Full Name")
phone = driver.find_element_by_name("mobile")
phone.send_keys("123456789")
btn_login = driver.find_element_by_id("newLoanButton")
btn_login.click()

#Step1 Page
driver.implicitly_wait(10)
inpt_birth = driver.find_element_by_name("birth")
inpt_birth.send_keys("11111990")
driver.implicitly_wait(10)
inpt_email = driver.find_element_by_name("email")
inpt_email.send_keys("email1234567890@gmail.com")
driver.implicitly_wait(10)
id_cmdn = driver.find_element_by_name("id_number")
id_cmdn.send_keys("123 456 789 000")
driver.implicitly_wait(10)
inpt_cmdn = driver.find_element_by_name("id_issue_date")
inpt_cmdn.send_keys("11111940")
driver.implicitly_wait(10)
gndr = driver.find_element_by_xpath("//label[contains(.,'Nữ')]")
gndr.click()
driver.implicitly_wait(10)
marital_status = driver.find_element_by_xpath("//div[7]/div/div/div/div")
marital_status.click()
martl_selct = driver.find_element_by_xpath("//li[5]")
martl_selct.click()
driver.implicitly_wait(10)
phone_brnd = driver.find_element_by_xpath("//div[8]/div/div/div/div")
phone_brnd.click()
phone_selct = driver.find_element_by_xpath("//li[contains(.,'Sony')]")
phone_selct.click()
driver.implicitly_wait(10)
btn_go = driver.find_element_by_xpath("//button[contains(.,'Tiếp tục')]")
btn_go.click()
#driver.quit()






