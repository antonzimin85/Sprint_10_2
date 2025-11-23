import pytest
from faker import Faker

from api.listing_api import ListingApi
from api.user_api import UserApi
from data.listing_data import ListingData


@pytest.fixture(scope="function")
def register_user_data():
    faker = Faker()
    password = faker.password(
        length=7, special_chars=False, upper_case=False, digits=False
    )
    user_data = {
        "email": f"{faker.email()}tstzim",
        "password": password,
        "submitPassword": password,
    }
    return user_data


@pytest.fixture(scope="function")
def login_user_data(register_user_data):
    user_data = {
        "email": register_user_data["email"],
        "password": register_user_data["password"],
    }
    return user_data


@pytest.fixture(scope="function")
def register_new_user(register_user_data):
    UserApi.register_new_user(register_user_data)


@pytest.fixture(scope="function")
def access_token(register_user_data):
    response = UserApi.register_new_user(register_user_data)
    return response.json()["access_token"]["access_token"]


@pytest.fixture(scope="function")
def listing_id_and_token(access_token):
    data = ListingData.UPDATE_LISTING_DATA.copy()
    response = ListingApi.create_listing(access_token, data)
    listing_id = response.json()["id"]
    return access_token, listing_id
