from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#lambdatest setup and opening the desired website
username = "Your LambdaTest Username"
accessToken = "Your LambdaTest Access Key"
gridUrl = "hub.lambdatest.com/wd/hub"
 
capabilities = {
    'LT:Options' : {
        "user" : "Your LambdaTest Username",
        "accessKey" : "Your LambdaTest Access Key",
        "build" : "your build name",
        "name" : "your test name",
        "platformName" : "Windows 11",
    },
    "browserName" : "Chrome",
    "browserVersion" : "103.0",
}
 
url = "https://"+username+":"+accessToken+"@"+gridUrl
 
browser = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capabilities
)

browser.maximize_window()
browser.get("https://www.lambdatest.com/selenium-playground/hover-demo")

# create action chain object
actions = ActionChains(browser)
actions.move_by_offset(617, 593)
actions.perform()

#closing the browser
browser.quit()