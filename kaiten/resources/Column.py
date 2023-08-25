import requests
from kaiten.resources.Resource import Resource

class Column(Resource):
    def __init__(self, columns_params_dict):
        super().__init__(columns_params_dict)