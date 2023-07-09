import requests
from kaiten.resources.Resource import Resource

class Card(Resource):
    def __init__(self, client, card_id, card_params_dict = None):
        if card_params_dict:
            # initializing Card from params_dict without doing new request
            super().__init__(card_params_dict)
            return
        self.api_url = f"{client.base_api_url}/cards/{card_id}"
        card_request = requests.get(self.api_url, headers=client.headers)
        card_request_dict = card_request.json()
        super().__init__(card_request_dict)