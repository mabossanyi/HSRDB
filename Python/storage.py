class Storage:
    # Attributes
    _types = list()
    _paths = list()
    _items = list()
    _items_sets = list()
    _characters_data = list()
    _stats = list()
    _slots = list()
    _characters = list()
    _characters_stats = list()
    _characters_items = list()

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

    def get_characters_data(self):
        return self._characters_data

    def get_stored_stats(self):
        return self._stats

    def get_stored_slots(self):
        return self._slots

    def get_stored_characters(self):
        return self._characters

    def get_stored_characters_stats(self):
        return self._characters_stats

    def get_stored_characters_items(self):
        return self._characters_items

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
            self._items_sets.append((id_item, quantity, description))

    def store_characters_raw_data(self, characters_data):
        self._characters_data = characters_data

    def store_stats(self, stats):
        id_stat = 1

        for stat in stats:
            self._stats.append((id_stat, stat))
            id_stat += 1

    def store_slots(self, slots):
        id_slot = 1

        for slot in slots:
            self._slots.append((id_slot, slot))
            id_slot += 1

    def store_characters(self, characters):
        id_character = 1

        for character in characters:
            (name, rarity, type, path) = character
            id_type = str([t[0] for t in self.get_stored_types() if type == t[1]][0])
            id_path = str([p[0] for p in self.get_stored_paths() if path == p[1]][0])
            self._characters.append((id_character, name, rarity, id_type, id_path))
            id_character += 1

    def store_characters_stats(self, characters_stats):
        for character_stat in characters_stats:
            (name, slot_name, stat) = character_stat
            id_character = str([c[0] for c in self.get_stored_characters() if name == c[1]][0])
            id_slot = str([sl[0] for sl in self.get_stored_slots() if slot_name == sl[1]][0])
            id_stat = str([st[0] for st in self.get_stored_stats() if stat == st[1]][0])
            self._characters_stats.append((id_character, id_slot, id_stat))

    def store_characters_items(self, characters_items):
        for character_item in characters_items:
            (name, slot_name, item_name, quantity) = character_item
            id_character = str([c[0] for c in self.get_stored_characters() if name == c[1]][0])
            id_slot = str([sl[0] for sl in self.get_stored_slots() if slot_name == sl[1]][0])
            id_item = str([it[0] for it in self.get_stored_items() if item_name == it[1]][0])
            self._characters_items.append((id_character, id_slot, id_item, quantity))
