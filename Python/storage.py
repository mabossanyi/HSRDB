class Storage:
    # Attributes
    _types = None
    _paths = None
    _items = None
    _item_sets = None
    _characters_data = None
    _stats = None
    _slots = None
    _characters = None
    _character_stats = None
    _character_items = None

    # Constructors
    def __init__(self):
        self._types = list()
        self._paths = list()
        self._items = list()
        self._item_sets = list()
        self._characters_data = list()
        self._stats = list()
        self._slots = list()
        self._characters = list()
        self._character_stats = list()
        self._character_items = list()

    # Getters
    def get_stored_types(self):
        return self._types

    def get_stored_paths(self):
        return self._paths

    def get_stored_items(self):
        return self._items

    def get_stored_item_sets(self):
        return self._item_sets

    def get_characters_data(self):
        return self._characters_data

    def get_stored_stats(self):
        return self._stats

    def get_stored_slots(self):
        return self._slots

    def get_stored_characters(self):
        return self._characters

    def get_stored_character_stats(self):
        return self._character_stats

    def get_stored_character_items(self):
        return self._character_items

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

    def store_item_sets(self, items_details):
        for item in items_details:
            (name, quantity, description) = item
            id_item = str([item[0] for item in self.get_stored_items()
                           if name == item[1]][0])
            self._item_sets.append((id_item, quantity, description))

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
            id_type = str([type_t[0] for type_t in self.get_stored_types()
                           if type == type_t[1]][0])
            id_path = str([path_p[0] for path_p in self.get_stored_paths()
                           if path == path_p[1]][0])
            self._characters.append((id_character, name, rarity,
                                     id_type, id_path))
            id_character += 1

    def store_character_stats(self, characters_stats):
        for character_stat in characters_stats:
            (name, slot_name, stat) = character_stat
            id_character = str(
                [character[0] for character in self.get_stored_characters()
                 if name == character[1]][0])
            id_slot = str([slot[0] for slot in self.get_stored_slots()
                           if slot_name == slot[1]][0])
            id_stat = str([stat_st[0] for stat_st in self.get_stored_stats()
                           if stat == stat_st[1]][0])
            self._character_stats.append((id_character, id_slot, id_stat))

    def store_character_items(self, characters_items):
        for character_item in characters_items:
            (name, slot_name, item_name, quantity) = character_item
            id_character = str(
                [character[0] for character in self.get_stored_characters()
                 if name == character[1]][0])
            id_slot = str([slot[0] for slot in self.get_stored_slots()
                           if slot_name == slot[1]][0])
            id_item = str([item[0] for item in self.get_stored_items()
                           if item_name == item[1]][0])
            self._character_items.append((id_character, id_slot,
                                          id_item, quantity))
