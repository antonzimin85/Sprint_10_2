import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

import config


class ListingApi:

    @staticmethod
    def create_listing(token, listing_data):
        m = MultipartEncoder(fields=listing_data)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": m.content_type}
        response = requests.post(
            config.CREATE_LISTING_ENDPOINT, headers=headers, data=m
        )
        return response

    @staticmethod
    def update_listing(token, listing_id, update_listing_data):
        update_url = f"{config.UPDATE_LISTING_ENDPOINT}/{listing_id}"
        m = MultipartEncoder(fields=update_listing_data)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": m.content_type}
        response = requests.patch(update_url, headers=headers, data=m)
        return response

    @staticmethod
    def delete_listing(token, listing_id):
        delete_url = f"{config.DELETE_LISTING_ENDPOINT}/{listing_id}"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.delete(delete_url, headers=headers)
        return response
