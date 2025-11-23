from api.listing_api import ListingApi
from data.error_messages import ErrorMessages
from data.listing_data import ListingData
from data.response_status import ResponseStatus
from data.success_messages import SuccessMessages


class TestListing:

    def test_create_listing_created_successfully(self, access_token):
        data = ListingData.LISTING_DATA.copy()
        response = ListingApi.create_listing(access_token, data)
        assert (
            response.status_code == ResponseStatus.CREATED
            and response.json()["name"] == data["name"]
        )

    def test_update_listing_updated_successfully(self, listing_id_and_token):
        token, listing_id = listing_id_and_token
        update_data = ListingData.UPDATE_LISTING_DATA.copy()
        response = ListingApi.update_listing(token, listing_id, update_data)
        assert (
            response.status_code == ResponseStatus.OK
            and response.json()["name"] == update_data["name"]
        )

    def test_update_listing_other_user_error_is_returned(self, access_token):
        listing_id = "1960"
        update_data = ListingData.UPDATE_LISTING_DATA.copy()
        response = ListingApi.update_listing(access_token, listing_id, update_data)
        assert (
            response.status_code == ResponseStatus.UNAUTHORIZED
            and response.json()["message"] == ErrorMessages.UNAUTHORIZED_ERROR_MESSAGE
        )

    def test_delete_listing_deleted_successfully(self, listing_id_and_token):
        token, listing_id = listing_id_and_token
        response = ListingApi.delete_listing(token, listing_id)
        assert (
            response.status_code == ResponseStatus.OK
            and response.json()["message"] == SuccessMessages.DELETE_LISTING_MESSAGE
        )
