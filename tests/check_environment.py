from pytest import mark

@mark.skip
def check_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80

def check_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    # driver.get(base_url)
    assert base_url == 'https://mydev-env.com'
    assert port == 8080

@mark.skip
def check_environment_is_stage(app_config):
    base_url = app_config.base_url
    assert base_url == 'stage'