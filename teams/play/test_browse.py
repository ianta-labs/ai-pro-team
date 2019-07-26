import time

from pytest import mark

@mark.ui
@mark.play
def test_can_browse_page(chrome_browser):
    my_browser = chrome_browser
    my_browser.get('https://w3ai.org')

    time.sleep(5)

    second_browser = chrome_browser
    second_browser.get('https://w3ai.net')

    assert True


