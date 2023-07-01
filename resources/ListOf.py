import requests
from resources.Space import Space

class ListOf:

    def __init__(self, client):
        self.client = client

    def spaces(self, ids_only = False):
        api_url = f"{self.client.base_api_url}/spaces"
        list_of_spaces = requests.get(api_url, headers=self.client.headers)
        list_of_spaces_dict = list_of_spaces.json()
        if ids_only:
            list_of_space_ids = list_of_spaces_dict[]
            return list_of_space_ids
        else:
            list_of_space_objects = []
            for space_id in list_of_spaces[]:
                list_of_space_objects += Space(self.client, space_id)
            return list_of_space_objects

    def users(self):
        return "users"

    def cards(self):
        # query required
        return "cards"

    def tags(self):
        return "tags"

    def card_types(self):
        return "card_types"

    def time_logs(self):
        return "time_logs"

    def properties(self):
        return "properties"

    def services(self):
        return "services"


