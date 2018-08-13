from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import code_saver
import time
import credential

LOGIN_PAGE_URL = "https://leetcode.com/accounts/login/"
SUBMIT_PAGE_URL = "https://leetcode.com/submissions/"
MAX_RUNS = 100

class Crawler:
    def login(self,browser):
        browser.get(LOGIN_PAGE_URL)
        elem = browser.find_element_by_name('login')
        elem.send_keys(credential.username)
        elem = browser.find_element_by_name('password')
        elem.send_keys(credential.password+ Keys.RETURN)

    def find_accepted_submissions(self):

        self.browser.get(SUBMIT_PAGE_URL)
        time.sleep(0.5)
        run = 0
        while True:
            accepted_submissions = self.browser.find_elements_by_link_text('Accepted')
            try:
                next_page = self.browser.find_element_by_partial_link_text('Older').get_attribute('href')
            except: #NoSuchElementException
                next_page = None
            submissions_list = map(lambda x:x.get_attribute('href'),accepted_submissions)
            for link in submissions_list:
                yield link
                run += 1
            if next_page:
                self.browser.get(next_page)
            else:
                break

    def open_new_tab(self,browser):
        browser.execute_script('''window.open("about:blank","_blank");''')

    def open_ac_submission_page(self,browser,url):
        browser.switch_to_window(browser.window_handles[1])
        browser.get(url)
        problem_name = browser.find_element_by_xpath('//*[@id="submission-app"]/div/div[1]/h4/a')
        code = browser.find_element_by_xpath('//*[@id="ace"]/div/div[3]/div/div[3]')
        language = browser.find_element_by_xpath('//*[@id="result_language"]')
        data = {"problem_name":problem_name.text,
                "language":language.text,
                "code":code.text}
        browser.switch_to_window(browser.window_handles[0])
        return data

    def setup_browser(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        self.open_new_tab(browser)
        browser.switch_to_window(browser.window_handles[0])
        self.browser = browser
        return browser

    def close_browser(self):
        self.browser.close()
        self.browser.quit()


crawler = Crawler()
browser = crawler.setup_browser()
saver = code_saver.CodeSaver()
crawler.login(browser)
time.sleep(2)
run = 0
for url in crawler.find_accepted_submissions():
    data = crawler.open_ac_submission_page(browser,url)
    saver.saveInstance(data)
    if run >= MAX_RUNS:
        browser.close()
        browser.quit()
        browser = crawler.setup_browser()
        crawler.login(browser)
        time.sleep(2)
        run = 0
    run += 1
     


browser.close()
browser.quit()