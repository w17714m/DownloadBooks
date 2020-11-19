from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, base64


def send_devtools(driver, cmd, params={}):
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    if 'status' in response:
        raise Exception(response.get('value'))
    return response.get('value')


def get_pdf_from_html(path, driver, print_options={}):
    driver.seleniumInstance.get(path)

    calculated_print_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'preferCSSPageSize': True,
    }
    calculated_print_options.update(print_options)
    result = send_devtools(driver.seleniumInstance, "Page.printToPDF", calculated_print_options)
    return base64.b64decode(result['data'])
