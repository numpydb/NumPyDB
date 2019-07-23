class Storage:
    storage = set()

    def add(self, data):
        self.storage.add(data)

    def getAll(self):
        return self.storage
