# Libraries
from urllib.request import urlopen
import extractor
import storage
import writer


if __name__ == '__main__':
    # Open the webpage
    url = "https://genshin.gg/star-rail/"
    page = urlopen(url)

    # Extract the HTML from the webpage
    html = page.read().decode("utf-8")

    # Get the classes "Extractor", "Storage" and "Writer"
    extractor = extractor.Extractor(html)
    storage = storage.Storage()
    writer = writer.Writer()

    # Extract the types
    types = extractor.extract_types()

    # Store the types
    storage.store_types(types)

    # Write the "INSERT_TYPE.sql" file
    writer.write_insert_type_sql_file("INSERT_TYPE.sql", storage)

    # Extract the path
    paths = extractor.extract_paths()

    # Store the paths
    storage.store_paths(paths)

    # Write the "INSERT_PATH.sql" file
    writer.write_insert_path_sql_file("INSERT_PATH.sql", storage)






