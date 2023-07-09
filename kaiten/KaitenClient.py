from kaiten.resources.Card import Card
from kaiten.resources.Space import Space
from kaiten.resources.Board import Board
from kaiten.resources.ListOf import ListOf
from kaiten.resources.User import User
from kaiten.resources.Property import Property


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

    def get_space(self, space_id):
        return Space(self, space_id)

    def get_board(self, board_id):
        return Board(self, board_id)

    def get_current_user(self):
        return User.get_current(self)

    def get_property(self, property_id):
        return Property(self, property_id)

    def list_of(self):
        return ListOf(self)
