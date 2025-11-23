import requests

import config


class UserApi:

    @staticmethod
    def register_new_user(user_data):
        response = requests.post(config.SIGN_UP_ENDPOINT, json=user_data)
        return response

    @staticmethod
    def login_user(user_data):
        response = requests.post(config.SIGN_IN_ENDPOINT, json=user_data)
        return response
