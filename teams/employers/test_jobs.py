from pytest import mark

@mark.smoke
@mark.jobs
class JobsTests:

    @mark.ui
    def test_can_navigate_to_jobs_page(self, chrome_browser):
        chrome_browser.get('https://ai-economy.web.app')
        assert True

    def test_culture(self):
        assert True

    def test_coolness(self):
        assert True


