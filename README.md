# Kaiten
Python Kaiten API client for convinient work with it

As this is an open-source project that is community maintained, do not be surprised if some bugs or features are not implemented quickly enough

# Quickstart
Just import client, authorize and get essences you need from the API. Then use it as a common python objects.
```
from KaitenClient import KaitenClient
client = KaitenClient(server =, token = )
card = client.get_card(card_id)
space = client.get_space(space_id)
board = client.get_board(board_id)
property = client.get_property(property_id)
```