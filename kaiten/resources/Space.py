from kaiten.resources.Resource import Resource
import requests
class Space(Resource):
    def __init__(self, client, space_id):
        self.api_url = f"{client.base_api_url}/spaces/{space_id}"
        space_request = requests.get(self.api_url, headers=client.headers)
        space_request_dict = space_request.json()
        super().__init__(space_request_dict)