import requests
from kaiten.resources.Resource import Resource

class SubColumn(Resource):
    def __init__(self, subcolumns_params_dict):
        super().__init__(subcolumns_params_dict)