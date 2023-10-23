class Storage:
    # Attributes
    _types = list()

    # Constructors
    def __init__(self):
        pass

    # Getters
    def get_stored_types(self):
        return self._types

    # Methods
    def store_types(self, types):
        id_type = 1

        for t in types:
            self._types.append((id_type, t))
            id_type += 1
