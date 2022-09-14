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
browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

time.sleep(5)

#locating the element
message_field = browser.find_element(By.ID, value="user-message")
button = browser.find_element(By.ID, value="showInput")
your_message = browser.find_element(By.ID, value="message")

# create action chain object
actions = ActionChains(browser)
actions.click(on_element=message_field)
actions.send_keys("Hello!")
actions.click(on_element=button)
actions.perform()

time.sleep(5)

#asserting that the message presented is Hello!
assert your_message.text == "Hello!"

time.sleep(5)

#closing the browser
browser.quit()

