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
browser.get("https://www.lambdatest.com/selenium-playground/drag-and-drop-demo")

time.sleep(5)

#locating the element
draggable = browser.find_element(By.XPATH, value="//p[normalize-space()='Drag me to my target']")
droparea = browser.find_element(By.XPATH, value="//div[@id='droppable']")

# create action chain object
actions = ActionChains(browser)
actions.drag_and_drop(draggable, droparea)
actions.perform()

time.sleep(5)

#asserting that when dropping, "Dropped!" is shown inside the droparea
message = browser.find_element(By.XPATH, value="//div[@id='droppable']/p")
assert message.text == "Dropped!"

time.sleep(5)

#closing the browser
browser.quit()

