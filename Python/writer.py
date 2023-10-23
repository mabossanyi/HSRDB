class Writer:
    # Attributes
    _is_insert_type_written = False

    # Constructors
    def __init__(self):
        self._is_insert_type_written = False

    # Getters
    def get_is_insert_type_written(self):
        return self._is_insert_type_written

    # Methods
    def write_insert_type_sql_file(self, file_name, storage):
        file = open(file_name, "w")
        stored_types = storage.get_stored_types()

        for (idType, type) in stored_types:
            file.write("INSERT INTO Type (idType, name, isDeleted) VALUES ({0} ,'{1}', false);\n"
                       .format(idType, type))

        self._is_insert_type_written = True
        file.close()
