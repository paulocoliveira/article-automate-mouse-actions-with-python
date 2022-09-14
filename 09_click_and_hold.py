from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.maximize_window()
browser.get("https://www.lambdatest.com/selenium-playground/drag-and-drop-demo")

#locating the element
draggabble_1 = browser.find_element(By.XPATH, value="//span[normalize-space()='Draggable 1']")

# create action chain object
actions = ActionChains(browser)
actions.click_and_hold(draggabble_1)
actions.perform()

#asserting that when dropping, "Dropped!" is shown inside the droparea
style = draggabble_1.get_attribute("style")
assert style.text == "Dropped!"

#closing the browser
browser.quit()