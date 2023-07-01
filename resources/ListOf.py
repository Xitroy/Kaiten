import requests
from resources.Space import Space

class ListOf:

    @staticmethod
    def spaces(client, ids_only = False):
        api_url = f"{client.base_api_url}/spaces"
        list_of_spaces = requests.get(api_url, headers=client.headers)
        list_of_spaces_dict = list_of_spaces.json()
        if ids_only:
            list_of_space_ids = list_of_spaces_dict[]
            return list_of_space_ids
        else:
            list_of_space_objects = []
            for space_id in list_of_spaces[]:
                list_of_space_objects += Space(client, space_id)
            return list_of_space_objects

    @staticmethod
    def users():
        return "users"

    @staticmethod
    def cards():
        # query required
        return "cards"

    @staticmethod
    def tags():
        return "tags"

    @staticmethod
    def card_types():
        return "card_types"

    @staticmethod
    def time_logs():
        return "time_logs"

    @staticmethod
    def properties():
        return "properties"

    @staticmethod
    def services():
        return "services"


