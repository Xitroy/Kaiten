# Kaiten
Python Kaiten API client for convenient work with it

As this is an open-source project that is community maintained, do not be surprised if some bugs or features are not implemented quickly enough

# Installation
```
pip install kaiten
```

# Quickstart
Just import client, authorize with a server and token. 
After that you can get essences you need from the API.
```
import kaiten
client = kaiten.KaitenClient(server =, token = )
```

## Get single resource
### Card
```
card = client.get_card(card_id)
```
### Space
```
space = client.get_space(space_id)
```

### Board
```
board = client.get_board(board_id)
```

### Current user
```
current_user = client.get_current_user()
```

### Property
```
property = client.get_property(property_id)
```
## Get list of resource
Use option: ids_only = True, if you need only id's to be represented in the list (list of Resource will be the default behavior)  
For example:
```
spaces = client.list_of().spaces(ids_only=True) # will return list of space ids
```
### List of spaces
```
spaces = client.list_of().spaces()
```

### List of users
```
users = client.list_of().users()
```

### List of tags
```
tags = client.list_of().tags()
```

### List of properties
```
properties = client.list_of().properties()
```

### List of lanes
```
lanes = client.list_of().lanes(board_id)
```