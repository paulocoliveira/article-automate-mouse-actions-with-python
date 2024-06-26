from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#lambdatest setup and opening the desired website
username = "Your LambdaTest Username"
accessToken = "Your LambdaTest Access Key"
gridUrl = "hub.lambdatest.com/wd/hub"
 
lt_options = {
    "user" : username,
    "accessKey" : accessToken,
    "build" : "your build name",
    "name" : "your test name",
    "platformName" : "Windows 11",
    "browserName" : "Chrome",
    "browserVersion" : "latest",
    "selenium_version": "latest"
}

web_driver = webdriver.ChromeOptions()
options = web_driver
options.set_capability('LT:Options', lt_options)

url = "https://"+username+":"+accessToken+"@"+gridUrl
browser = webdriver.Remote(
    command_executor=url,
    options=options
)

browser.maximize_window()
browser.get("https://www.lambdatest.com/selenium-playground/hover-demo")

#locating the element
first_image = browser.find_element(By.XPATH, value="//div[@class='s__column m-15']//img")

# create action chain object
actions = ActionChains(browser)
actions.move_to_element(first_image)
actions.perform()

from time import sleep
sleep(10)

#asserting that when hoving, "Hover" is shown below the image
message = browser.find_element(By.XPATH, value="//div[@class='s__column m-15']//p")
assert message.text == "Hover"

#closing the browser
browser.quit()