from api.user_api import UserApi
from data.error_messages import ErrorMessages
from data.response_status import ResponseStatus


class TestUser:

    def test_user_sign_up_user_successfully_signed_up(self, register_user_data):
        response = UserApi.register_new_user(register_user_data)
        user_email = response.json()["user"]["email"]
        assert (
            response.status_code == ResponseStatus.CREATED
            and user_email == register_user_data["email"]
        )

    def test_user_sign_up_existing_user_error_is_returned(self, register_user_data, access_token):
        response = UserApi.register_new_user(register_user_data)
        error_message = response.json()["message"]
        assert response.status_code == ResponseStatus.BAD_REQUEST
        assert error_message == ErrorMessages.USER_EXISTS_ERROR_MESSAGE

    def test_user_login_user_is_successfully_logged_in(self, register_user_data):
        UserApi.register_new_user(register_user_data)
        login_user_data = {
            'email': register_user_data['email'],
            'password': register_user_data['password']
        }
        response = UserApi.login_user(login_user_data)
        token = response.json()["token"]["access_token"]
        assert response.status_code == ResponseStatus.CREATED and token is not None
