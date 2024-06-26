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
browser.get("https://www.lambdatest.com/selenium-playground/drag-and-drop-demo")

#locating the element
draggable = browser.find_element(By.XPATH, value="//p[normalize-space()='Drag me to my target']")
droparea = browser.find_element(By.XPATH, value="//div[@id='droppable']")

# create action chain object
actions = ActionChains(browser)
actions.drag_and_drop(draggable, droparea)
actions.perform()

#asserting that when dropping, "Dropped!" is shown inside the droparea
message = browser.find_element(By.XPATH, value="//div[@id='droppable']/p")
assert message.text == "Dropped!"

#closing the browser
browser.quit()

