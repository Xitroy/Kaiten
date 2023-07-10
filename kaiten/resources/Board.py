from kaiten.resources.Resource import Resource
import requests
class Board(Resource):
    def __init__(self, client, board_id):
        self.api_url = f"{client.base_api_url}/boards/{board_id}"
        board_request = requests.get(self.api_url, headers=client.headers)
        board_request_dict = board_request.json()
        super().__init__(board_request_dict)