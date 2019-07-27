class Config():
    def __init__(self, env):

        self.base_url = {
            'dev': 'https://mydev-env.com',
            'qa': 'https://myqa-env.com'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]




'''
------------------------------------ Code snippets for later use --------------
        SUPPORTED_ENVS = ['dev', 'qa']

        if env.lower() not in SUPPORTED_ENVS
            raise Exception(f'{env} is not a supported environment (supported envs: {SUPPORTED_ENVS})')
'''