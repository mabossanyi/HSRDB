# Libraries
from datetime import datetime
import os.path


class Writer:
    # Attributes
    _is_insert_file_written = None

    # Constructors
    def __init__(self):
        self._is_insert_file_written = False

    # Getters
    def get_is_insert_file_written(self):
        return self._is_insert_file_written

    # Methods
    def write_insert_sql_file(self, file_name, version, storage):
        sql_folder_path = "../SQL/"
        file_path = os.path.join(sql_folder_path, file_name)
        file = open(file_path, "w")

        self._write_file_header(file, version)
        self._write_insert_type_sql_file(file, storage)
        self._write_insert_path_sql_file(file, storage)
        self._write_insert_item_sql_file(file, storage)
        self._write_insert_items_set_sql_file(file, storage)
        self._write_insert_stat_sql_file(file, storage)
        self._write_insert_slot_sql_file(file, storage)
        self._write_insert_character_sql_file(file, storage)
        self._write_insert_character_stat_sql_file(file, storage)
        self._write_insert_character_item_sql_file(file, storage)
        self._is_insert_file_written = True

        file.close()

    def _write_file_header(self, file, version):
        file.write("/*\n")
        file.write("\tAuthor: Marc-Andre Bossanyi\n")
        file.write("\tEmail: ma.bossanyi@gmail.com\n")
        file.write("\tCreation Date: 2023/11/06\n")
        file.write("\tLast Updated: {}\n".
                   format(datetime.today().strftime('%Y/%m/%d')))
        file.write("\tHonkai: Star Rail - {}\n".format(version))
        file.write("*/\n\n")

    def _write_insert_type_sql_file(self, file, storage):
        file.write('-- Script INSERT for the table "Type"\n')
        stored_types = storage.get_stored_types()

        for (id_type, type) in stored_types:
            file.write("INSERT INTO Type (idType, name, isDeleted) "
                       "VALUES ({} ,'{}', false);\n"
                       .format(id_type, type))

        file.write("\n")

    def _write_insert_path_sql_file(self, file, storage):
        file.write('-- Script INSERT for the table "Path"\n')
        stored_paths = storage.get_stored_paths()

        for (id_path, path) in stored_paths:
            file.write("INSERT INTO Path (idPath, name, isDeleted) "
                       "VALUES ({}, '{}', false);\n"
                       .format(id_path, path))

        file.write("\n")

    def _write_insert_item_sql_file(self, file, storage):
        file.write('-- Script INSERT for the table "Item"\n')
        stored_items = storage.get_stored_items()

        for (id_item, item) in stored_items:
            file.write("INSERT INTO Item (idItem, name, isDeleted) "
                       "VALUES ({}, '{}', false);\n"
                       .format(id_item, item))

        file.write("\n")

    def _write_insert_items_set_sql_file(self, file, storage):
        file.write('-- Script INSERT for the table "ItemsSet"\n')
        stored_items_set = storage.get_stored_items_set()

        for (id_item, quantity, description) in stored_items_set:
            file.write("INSERT INTO ItemsSet (idItem, quantity, description) "
                       "VALUES ({}, {}, '{}');\n"
                       .format(id_item, quantity, description))

        file.write("\n")

    def _write_insert_stat_sql_file(self, file, storage):
        file.write('-- Script INSERT for the table "Stat"\n')
        stored_stats = storage.get_stored_stats()

        for (id_stat, stat) in stored_stats:
            file.write("INSERT INTO Stat (idStat, name, isDeleted) "
                       "VALUES ({}, '{}', false);\n"
                       .format(id_stat, stat))

        file.write("\n")

    def _write_insert_slot_sql_file(self, file, storage):
        file.write('-- Script INSERT for the table "Slot"\n')
        stored_slots = storage.get_stored_slots()

        for (id_slot, slot) in stored_slots:
            file.write("INSERT INTO Slot (idSlot, name, isDeleted) "
                       "VALUES ({}, '{}', false);\n"
                       .format(id_slot, slot))

        file.write("\n")

    def _write_insert_character_sql_file(self, file, storage):
        file.write('-- Script INSERT for the table "Character"\n')
        stored_characters = storage.get_stored_characters()

        for (id_character, name, rarity, id_type, id_path) \
                in stored_characters:
            file.write("INSERT INTO Character (idCharacter, name, rarity, "
                       "idType, idPath, isOwned, isDeleted) "
                       "VALUES ({}, '{}', {}, {}, {}, false, false);\n"
                       .format(id_character, name, rarity, id_type, id_path))

        file.write("\n")

    def _write_insert_character_stat_sql_file(self, file, storage):
        file.write('-- Script INSERT for the table "CharacterStat"\n')
        stored_characters_stats = storage.get_stored_characters_stats()

        for (id_character, id_slot, id_stat) \
                in stored_characters_stats:
            file.write("INSERT INTO CharacterStat ("
                       "idCharacter, idSlot, idStat) "
                       "VALUES ({}, {}, {});\n"
                       .format(id_character, id_slot, id_stat))

        file.write("\n")

    def _write_insert_character_item_sql_file(self, file, storage):
        file.write('-- Script INSERT for the table "CharacterItem"\n')
        stored_characters_items = storage.get_stored_characters_items()

        for (id_character, id_slot, id_stat, quantity) \
                in stored_characters_items:
            file.write("INSERT INTO CharacterItem ("
                       "idCharacter, idSlot, idItem) "
                       "VALUES ({}, {}, {});\n"
                       .format(id_character, id_slot, id_stat))

        file.write("\n")
