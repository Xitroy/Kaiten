import requests
from Resource import Resource
class Card(Resource):
    def __init__(self, client, card_id):
        self.api_url = f"{client.base_api_url}/cards/{card_id}"
        card_request = requests.get(self.api_url)
        card_request_dict = card_request.json()
        super().__init__(card_request_dict)