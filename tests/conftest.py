from pytest import fixture

from config import Config

from selenium import webdriver

# ---------------- Jul 27, 2019 - pytest course ---------------------
def pytest_addoption(parser):
    parser.addoption(
	"--env",
	action="store",
	default="dev",
	help="Environment to run tests against"
	)

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg

'''
scope='function' - for each test function
scope='session' - for the entire test session / all functions eg. same browser instance
'''
@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser       # or return

    # teardown - everything after yield
    print('I am tearing down this browser')

# ToDo - add webdriver.Firefox & webdriver.Edge
# test will be run for each item inn the params list
@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()
