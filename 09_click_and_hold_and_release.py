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
browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

#locating the element
message_field = browser.find_element(By.ID, value="user-message")
button = browser.find_element(By.ID, value="showInput")
your_message = browser.find_element(By.ID, value="message")

# create action chain object
actions = ActionChains(browser)
actions.click(on_element=message_field)
actions.send_keys("Hello!")
actions.click_and_hold(button)
actions.release()
actions.perform()

#asserting that the message presented is Hello!
assert your_message.text == "Hello!"

#closing the browser
browser.quit()

