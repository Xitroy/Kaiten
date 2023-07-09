from kaiten.resources.Resource import Resource

class Tag(Resource):
    def __init__(self, tag_params_dict):
        # There is no Tag essence in terms of getting one (current user only exists in API)
        # so signature is a bit differs from other Resource
        super().__init__(tag_params_dict)