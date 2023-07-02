from resources.Card import Card
from resources.Space import Space
from resources.Board import Board
from resources.ListOf import ListOf
from resources.User import User
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

    def list_of(self):
        return ListOf(self)
