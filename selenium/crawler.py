from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import credential

LOGIN_PAGE_URL = "https://leetcode.com/accounts/login/"
SUBMIT_PAGE_URL = "https://leetcode.com/submissions/"


def login(browser):
    browser.get(LOGIN_PAGE_URL)
    elem = browser.find_element_by_name('login')
    elem.send_keys(credential.username)
    elem = browser.find_element_by_name('password')
    elem.send_keys(credential.password+ Keys.RETURN)

def find_accepted_submissions(browser):

    browser.get(SUBMIT_PAGE_URL)
    while True:
        accepted_submissions = browser.find_element_by_link_text('Accepted')
        try:
            next_page = browser.find_element_by_partial_link_text('Older')
        except: #NoSuchElementException
            next_page = None
        for link in accepted_submissions:
            yield link.get_attribute('href')
        if next_page:
            next_page.click()

def open_new_tab(browser):
    browser.execute_script('''window.open("about:blank","_blank");''')

def open_ac_submission_page(browser,url):
    browser.switch_to_window(browser.window_handles[1])
    browser.get(url)
    browser.switch_to_window(browser.window_handles[0])



browser = webdriver.Firefox()
open_new_tab(browser)
browser.switch_to_window(browser.window_handles[0])
login(browser)
time.sleep(2)
for url in find_accepted_submissions(browser):
#     open_ac_submission_page(url)
     time.sleep(0.5)



#browser.quit()