class Writer:
    # Attributes
    _is_insert_type_written = False
    _is_insert_path_written = False
    _is_insert_item_written = False
    _is_insert_items_set_written = False
    _is_insert_stat_written = False

    # Constructors
    def __init__(self):
        self._is_insert_type_written = False
        self._is_insert_path_written = False
        self._is_insert_item_written = False
        self._is_insert_items_set_written = False
        self._is_insert_stat_written = False

    # Getters
    def get_is_insert_type_written(self):
        return self._is_insert_type_written

    # Methods
    def write_insert_type_sql_file(self, file_name, storage):
        file = open(file_name, "w")
        stored_types = storage.get_stored_types()

        for (id_type, type) in stored_types:
            file.write("INSERT INTO Type (idType, name, isDeleted) VALUES ({0} ,'{1}', false);\n"
                       .format(id_type, type))

        self._is_insert_type_written = True
        file.close()

    def write_insert_path_sql_file(self, file_name, storage):
        file = open(file_name, "w")
        stored_paths = storage.get_stored_paths()

        for (id_path, path) in stored_paths:
            file.write("INSERT INTO Path (idPath, name, isDeleted) VALUES ({0}, '{1}', false);\n"
                       .format(id_path, path))

        self._is_insert_path_written = True
        file.close()

    def write_insert_item_sql_file(self, file_name, storage):
        file = open(file_name, "w")
        stored_items = storage.get_stored_items()

        for (id_item, item) in stored_items:
            file.write("INSERT INTO Item (idItem, name, isDeleted) VALUES ({0}, '{1}', false);\n"
                       .format(id_item, item))

        self._is_insert_item_written = True
        file.close()

    def write_insert_items_set_sql_file(self, file_name, storage):
        file = open(file_name, "w")
        stored_items_set = storage.get_stored_items_set()

        for (id_item, quantity, description) in stored_items_set:
            file.write("INSERT INTO ItemsSet (idItem, quantity, description) VALUES ({0}, {1}, '{2}');\n"
                       .format(id_item, quantity, description))

        self._is_insert_items_set_written = True
        file.close()

    def write_insert_stat_sql_file(self, file_name, storage):
        file = open(file_name, "w")
        stored_stats = storage.get_stored_stats()

        for (id_stat, stat) in stored_stats:
            file.write("INSERT INTO Stat (idStat, name, isDeleted) VALUES ({0}, '{1}', false);\n"
                       .format(id_stat, stat))

        self._is_insert_stat_written = True
        file.close()
