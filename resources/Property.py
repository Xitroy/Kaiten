import requests
from resources.Resource import Resource


class Property(Resource):
    def __init__(self, client, property_id, property_params_dict = None):
        if property_params_dict:
            # initializing Property from params_dict without doing new request
            super().__init__(property_params_dict)
            return
        self.api_url = f"{client.base_api_url}/company/custom-properties/{property_id}"
        property_request = requests.get(self.api_url, headers=client.headers)
        property_request_dict = property_request.json()
        super().__init__(property_request_dict)

