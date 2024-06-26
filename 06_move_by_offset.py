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

# create action chain object
actions = ActionChains(browser)
actions.move_by_offset(617, 593)
actions.perform()

#closing the browser
browser.quit()