import requests
from resources.Space import Space
from resources.Property import Property
from resources.User import User

class ListOf:

    def __init__(self, client):
        self.client = client

    def spaces(self, ids_only = False):
        api_url = f"{self.client.base_api_url}/spaces"
        list_of_spaces_request = requests.get(api_url, headers=self.client.headers)
        list_of_spaces = list_of_spaces_request.json()
        list_of_space_ids = [i['id'] for i in list_of_spaces]
        if ids_only:
            return list_of_space_ids
        else:
            return [Space(self.client, i) for i in list_of_space_ids]

    def users(self, ids_only = False):
        api_url = f"{self.client.base_api_url}/users"
        list_of_users_request = requests.get(api_url, headers=self.client.headers)
        list_of_users_dict = list_of_users_request.json()
        list_of_user_ids = [i['id'] for i in list_of_users_dict]
        if ids_only:
            return list_of_user_ids
        else:
            return [User(i) for i in list_of_users_dict]

    def cards(self):
        # query required
        return "cards"

    def tags(self):
        return "tags"

    def card_types(self):
        return "card_types"

    def time_logs(self):
        return "time_logs"

    def properties(self, ids_only = False):
        api_url = f"{self.client.base_api_url}/company/custom-properties"
        list_of_properties_request = requests.get(api_url, headers=self.client.headers)
        list_of_properties = list_of_properties_request.json()
        list_of_properties_ids = [i['id'] for i in list_of_properties]
        if ids_only:
            return list_of_properties_ids
        else:
            return [Property(self.client, i) for i in list_of_properties_ids]

    def services(self):
        return "services"


