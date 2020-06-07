from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
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
driver.implicitly_wait(20)
inpt_birth = driver.find_element_by_name("birth")
inpt_birth.send_keys("11111990")
driver.implicitly_wait(20)
inpt_email = driver.find_element_by_name("email")
inpt_email.send_keys("email1234567890@gmail.com")
driver.implicitly_wait(20)
id_cmdn = driver.find_element_by_name("id_number")
id_cmdn.send_keys("123 456 789 000")
driver.implicitly_wait(20)
inpt_cmdn = driver.find_element_by_name("id_issue_date")
inpt_cmdn.send_keys("11111940")
driver.implicitly_wait(20)
gndr = driver.find_element_by_xpath("//label[contains(.,'Nữ')]")
gndr.click()
driver.implicitly_wait(20)
marital_status = driver.find_element_by_xpath("//div[7]/div/div/div/div")
marital_status.click()
martl_selct = driver.find_element_by_xpath("//li[5]")
martl_selct.click()
driver.implicitly_wait(20)
phone_brnd = driver.find_element_by_xpath("//div[8]/div/div/div/div")
phone_brnd.click()
phone_selct = driver.find_element_by_xpath("//li[contains(.,'Sony')]")
phone_selct.click()
driver.implicitly_wait(20)
btn_go = driver.find_element_by_xpath("//button[contains(.,'Tiếp tục')]")
btn_go.click()

#Step 2 Page
# btn_geo = driver.find_element_by_xpath("//span[contains(.,'Chỉ vị trí')]")
# btn_geo.click()
# driver.implicitly_wait(20)
# alert = browser.switch_to.alert
# alert.accept()
# confirm = browser.switch_to.alert
# confirm.accept()
# btn_go1 = driver.find_element_by_xpath("//div[3]/div[2]/button")
# btn_go1.click()
province = driver.find_element_by_xpath("//form[@id='step3']/div[2]/div[2]/div/div/div/div/div")
province.click()
driver.implicitly_wait(20)
selct_prvnce = driver.find_element_by_css_selector("#step3 > div:nth-child(4) > div.hidden-mobile.w-100p > div:nth-child(2) > div > div.jq-selectbox.jqselect.forms__input.forms__input--need.select-one.dropdown.opened.forms__input--invalid > div.jq-selectbox__dropdown > ul > li:nth-child(3)")
selct_prvnce.click()



screenshot_name = "screenshot_name.png"
driver.save_screenshot(screenshot_name)

#driver.quit()






