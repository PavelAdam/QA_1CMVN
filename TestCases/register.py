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
inpt_birth = driver.find_element_by_name("birth")
inpt_birth.send_keys("11111990")
inpt_email = driver.find_element_by_name("email")
inpt_email.send_keys("email1234567890@gmail.com")
id_cmdn = driver.find_element_by_name("id_number")
id_cmdn.send_keys("123 456 789 000")
inpt_cmdn = driver.find_element_by_name("id_issue_date")
inpt_cmdn.send_keys("11111940")
gndr = driver.find_element_by_xpath("//form[@id='step2']/div[2]/div[6]/div/p/label")
gndr.send_keys()

#driver.quit()






