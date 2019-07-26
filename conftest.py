from pytest import fixture

from selenium import webdriver

'''
scope='function' - for each test function
scope='session' - for the entire test session / all functions eg. same browser instance
'''
@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser       # or return

    # teardown
    print('I am tearing down this browser')

