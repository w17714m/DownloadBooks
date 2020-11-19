import time
import os
from selenium.webdriver.common.by import By
from seleniumImpl.seleniumInstance import SeleniumDownload



#from selenium.webdriver.chrome.options
# variables secretas app
urlToDownload = os.getenv('URL_TO_DOWNLOAD')
user = os.getenv('USER')
password = os.getenv('PASSWORD')


def get_all_urls(session, url):
    temp = []

    session.seleniumInstance.implicitly_wait(2)
    if isinstance(session, SeleniumDownload):

        session.seleniumInstance.get(urlToDownload)

        # email
        email_element = session.seleniumInstance.find_element_by_name('email')
        email_element.send_keys(user)

        # pass
        pass_element = session.seleniumInstance.find_element_by_name('password')
        pass_element.send_keys(password)

        # button
        pass_element = session.seleniumInstance.find_element_by_class_name('src-Button-button')
        pass_element.click()

        time.sleep(3)

        session.seleniumInstance.get(url)

        time.sleep(2)

        temp.append({"cookies": session.seleniumInstance.get_cookies()})

        list_element = session.seleniumInstance.find_element(By.CLASS_NAME, 'detail-toc')
        elems = list_element.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            if 'xhtml' in elem.get_attribute("href"):
                temp.append(
                    {
                        "path": elem.get_attribute("href"),
                        "name": elem.text
                    }
                )
        return temp
