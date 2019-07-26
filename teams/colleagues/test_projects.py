from pytest import mark

@mark.ui
@mark.smoke
@mark.projects
class ProjectsTests:

    def test_can_navigate_to_projects_page(self, chrome_browser):
        chrome_browser.get('https://w3ai.org')
        assert True

    def test_budget(self):
        assert True

    def test_coolness(self):
        assert True
