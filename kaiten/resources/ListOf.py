import requests
from kaiten.resources.Space import Space
from kaiten.resources.Property import Property
from kaiten.resources.User import User
from kaiten.resources.Tag import Tag
from kaiten.resources.Card import Card
from kaiten.resources.SubColumn import SubColumn
from kaiten.resources.Column import Column

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

    def cards(self, ids_only = False, **query):
        # query required
        # Please consider to read the docs for understanding query
        # https://developers.kaiten.ru/cards/retrieve-card-list
        # TODO there is small difference with a card from these request and when you try to get single card
        api_url = f"{self.client.base_api_url}/cards"
        list_of_cards_request = requests.get(api_url, headers=self.client.headers, params=query)
        list_of_cards_dict = list_of_cards_request.json()
        list_of_cards_ids = [i['id'] for i in list_of_cards_dict]
        if ids_only:
            return list_of_cards_ids
        else:
            return [Card(None, None, card_params_dict=i) for i in list_of_cards_dict]

    def tags(self, ids_only = False):
        api_url = f"{self.client.base_api_url}/tags"
        list_of_tags_request = requests.get(api_url, headers=self.client.headers)
        list_of_tags_dict = list_of_tags_request.json()
        list_of_tags_ids = [i['id'] for i in list_of_tags_dict]
        if ids_only:
            return list_of_tags_ids
        else:
            return [Tag(i) for i in list_of_tags_dict]

    def card_types(self):
        return "card_types"

    def time_logs(self):
        return "time_logs"

    def properties(self, ids_only = False):
        api_url = f"{self.client.base_api_url}/company/custom-properties"
        list_of_properties_request = requests.get(api_url, headers=self.client.headers)
        list_of_properties_dict = list_of_properties_request.json()
        list_of_properties_ids = [i['id'] for i in list_of_properties_dict]
        if ids_only:
            return list_of_properties_ids
        else:
            return [Property(None, None, i) for i in list_of_properties_dict]

    def columns(self, ids_only = False, board_id):
        api_url = f"{self.client.base_api_url}/boards/{board_id}/columns"
        list_of_columns_request = requests.get(api_url, headers=self.client.headers)
        list_of_columns_dict = list_of_columns_request.json()
        list_of_columns_ids = [i['id'] for i in list_of_columns_dict]
        if ids_only:
            return list_of_columns_ids
        else:
            return [Column(None, None, i) for i in list_of_properties_dict]
    
    def subcolumns(self, ids_only = False, column_id):
        api_url = f"{self.client.base_api_url}/columns/{column_id}/subcolumns"
        list_of_subcolumns_request = requests.get(api_url, headers=self.client.headers)
        list_of_subcolumns_dict = list_of_subcolumns_request.json()
        list_of_subcolumns_ids = [i['id'] for i in list_of_subcolumns_dict]
        if ids_only:
            return list_of_subcolumns_ids
        else:
            return [SubColumn(None, None, i) for i in list_of_subcolumns_dict]

    def services(self):
        return "services"


