class Data:
    value = ""
    vector = []
    id = -1

    def __init__(self, vector, value, id_data=-1):
        self.vector = vector
        self.value = value
        if id_data:
            self.id = id_data

    def get(self):
        return {
            'value': self.value,
            'vector': self.vector,
            'id': self.id
        }
