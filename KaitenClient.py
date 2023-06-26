from resources.Card import Card
class KaitenClient:

    DEFAULT_OPTIONS = {

    }

    def __init__(self, server, token):
        self.server = server
        self.token = token

        self.headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': f'Bearer {self.token}',
        }

        self.base_api_url = f"{self.server}/api/latest"

    def get_card(self, card_id):
        return Card(self, card_id)