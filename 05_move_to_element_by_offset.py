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

#locating the element
first_image = browser.find_element(By.XPATH, value="//div[@class='s__column m-15']//img")

# create action chain object
actions = ActionChains(browser)
actions.move_to_element_with_offset(first_image, 100, 200)
actions.perform()

time.sleep(5)

#asserting that when hoving, "Hover" is shown below the image
message = browser.find_element(By.XPATH, value="//div[@class='s__column m-15']//p")

assert message.text == "Hover"

time.sleep(5)

#closing the browser
browser.quit()

