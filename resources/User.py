import requests
from resources.Resource import Resource

class User(Resource):
    def __init__(self, user_params_dict):
        # There is no User essence in terms of getting one (current user only exists in API)
        # so signature is a bit differs from other Resource
        super().__init__(user_params_dict)

    @staticmethod
    def get_current(client):
        api_url = f"{client.base_api_url}/users/current"
        current_user_request = requests.get(api_url, headers=client.headers)
        current_user_request_dict = current_user_request.json()
        return User(current_user_request_dict)