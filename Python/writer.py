class Writer:
    # Attributes
    _is_insert_type_written = False
    _is_insert_path_written = False
    _is_insert_item_written = False

    # Constructors
    def __init__(self):
        self._is_insert_type_written = False
        self._is_insert_path_written = False
        self._is_insert_item_written = False

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
            file.write("INSERT INTO Path (idPath, name, isDeleted VALUES ({0}, '{1}', false);\n"
                       .format(id_path, path))

        self._is_insert_path_written = True
        file.close()

    def write_insert_item_sql_file(self, file_name, storage):
        file = open(file_name, "w")
        stored_items = storage.get_stored_items()

        for (id_item, item) in stored_items:
            file.write("INSERT INTO Item (idItem, name, isDeleted VALUES ({0}, '{1}', false);\n"
                       .format(id_item, item))

        self._is_insert_item_written = True
        file.close()