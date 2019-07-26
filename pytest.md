# Pytest

### pytest.ini

[pytest]
python_files = test_*
python_classes = *Tests
python_functions = test_*

##Test Searching

from pytest import mark

https://docs.pytest.org/en/latest/example/markers.html

@mark.smoke
@mark.engine
def test_..._

// test only marks
pytest -m engine
pytest -m smoke

pytest -m "engine or smoke"

pytest -m "not entertainment"

// Summary of markers as documented on pytest.ini !!! 
pytest --markers

## Test Fixtures

conftest.py

from pytest import fixture

from selenium import webdriver

'''
scope='function' - for each test function
scope='session' - for the entire test session / all functions eg. same browser instance
'''
@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser       # or return

    # teardown
    print('I am tearing down this browser')
	
----

// -s - for showing console prints
// -v - verbose
pytest -m ui -s -v





