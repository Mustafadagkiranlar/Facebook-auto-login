"""
Source of video is == https://www.youtube.com/watch?v=f7LEWxX4AVI
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://facebook.com')

email = str(input('Enter your email: '))


mail = driver.find_element_by_xpath('//*[@id="email"]')
mail.send_keys(email)

password = str(input('Enter your password: '))

psw = driver.find_element_by_xpath('//*[@id="pass"]')
psw.send_keys(password)

loginButton = driver.find_element_by_xpath('//*[@id="u_0_b"]')
loginButton.click()
