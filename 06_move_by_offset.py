import time
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

time.sleep(5)

# create action chain object
actions = ActionChains(browser)
actions.move_by_offset(617, 593)
actions.perform()

time.sleep(5)

#closing the browser
browser.quit()

# import webdriver
from selenium import webdriver
   
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
   
# create webdriver object
driver = webdriver.Firefox()
   
# create action chain object
action = ActionChains(driver)