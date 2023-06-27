import requests
from Resource import Resource


class Property(Resource):
    def __init__(self, client, property_id):
        self.api_url = f"{client.base_api_url}/company/custom-properties/{property_id}"
        property_request = requests.get(self.api_url, headers=client.headers)
        property_request_dict = property_request.json()
        super().__init__(property_request_dict)

