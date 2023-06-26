class Resource:

    def __init__(self, data):
        self.__dict__.update(data)

    def __getattr__(self, name):
        return self.__dict__[name]


