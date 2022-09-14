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
browser.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

time.sleep(5)

#locating the element
age_sorting = browser.find_element(By.XPATH, value="//th[@aria-label='Age: activate to sort column ascending']")

# create action chain object
actions = ActionChains(browser)
actions.double_click(age_sorting)
actions.perform()

time.sleep(5)

#asserting that the first two values are 66
first_age = browser.find_element(By.XPATH, value="//tr[1]//td[@class='sorting_1']")
second_age = browser.find_element(By.XPATH, value="//tr[2]//td[@class='sorting_1']")

assert first_age.text == "66"
assert second_age.text == "66"

time.sleep(5)

#closing the browser
browser.quit()

