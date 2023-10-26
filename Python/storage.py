class Storage:
    # Attributes
    _types = list()
    _paths = list()
    _items = list()
    _items_sets = list()


    # Constructors
    def __init__(self):
        pass

    # Getters
    def get_stored_types(self):
        return self._types

    def get_stored_paths(self):
        return self._paths

    def get_stored_items(self):
        return self._items

    def get_stored_items_set(self):
        return self._items_sets

    # Methods
    def store_types(self, types):
        id_type = 1

        for type in types:
            self._types.append((id_type, type))
            id_type += 1

    def store_paths(self, paths):
        id_path = 1

        for path in paths:
            self._paths.append((id_path, path))
            id_path += 1

    def store_items(self, items):
        id_item = 1

        for item in items:
            self._items.append((id_item, item))
            id_item += 1

    def store_items_sets(self, items_details):
        for item in items_details:
            (name, quantity, description) = item
            id_item = str([i[0] for i in self.get_stored_items() if name == i[1]][0])
            description = description.replace("'", "''")
            self._items_sets.append((id_item, quantity, description))
