class Storage:
    # Attributes
    _types = list()
    _paths = list()

    # Constructors
    def __init__(self):
        pass

    # Getters
    def get_stored_types(self):
        return self._types

    def get_stored_paths(self):
        return self._paths

    # Methods
    def store_types(self, types):
        id_type = 1

        for t in types:
            self._types.append((id_type, t))
            id_type += 1

    def store_paths(self, paths):
        id_path = 1

        for p in paths:
            self._paths.append((id_path, p))
            id_path += 1