# Libraries
import browser
import extractor
import processor
from storage import Storage
from writer import Writer


# Methods
def main():
    # Header of the program
    version = "1.5 (Phase 1)"
    print("Running the Honkai: Star Rail Database (HSRDB) script using "
          "the version '{}'\n".format(version))

    # Get the class "Extractor" for the main page using the URL
    # to extract the HTML
    main_page_url = "https://genshin.gg/star-rail/"
    main_page_extractor = get_page_extractor_from_url(main_page_url)

    # Get the classes "Storage" and "Writer"
    storage = Storage()

    # Extract and store the types
    print("Extracting and storing the types...")
    extract_and_store_types(main_page_extractor, storage)

    # Extract and store the paths
    print("Extracting and storing the paths...")
    extract_and_store_paths(main_page_extractor, storage)

    # Get the class "Extractor" for the relics page using the URL
    # to extract the HTML
    relics_page_url = "https://genshin.gg/star-rail/relics/"
    relics_page_extractor = get_page_extractor_from_url(relics_page_url)

    # Get the class "Extractor" for the ornaments page using the URL
    # to extract the HTML
    ornaments_page_url = "https://genshin.gg/star-rail/planar-ornaments/"
    ornaments_page_extractor = get_page_extractor_from_url(ornaments_page_url)

    # Extract and store the items (i.e. the relic names and ornament names)
    print("Extracting and storing the items (relics & ornaments)...")
    extract_and_store_items(
        relics_page_extractor, ornaments_page_extractor, storage)

    # Extract and store the items sets (i.e. relic sets description and
    # ornament sets description)
    print("Extracting and storing the items sets...")
    extract_and_store_items_sets(
        relics_page_extractor, ornaments_page_extractor, storage)

    # Extract and store the characters data for each character on the main page
    print("Extracting and storing the characters data for each character...")
    extract_and_store_characters_data(
        main_page_url, main_page_extractor, storage)

    # Get the class "Processor" from the characters raw data
    data_processor = processor.Processor(storage.get_characters_data())

    # Preprocess and store stats from the characters data
    print("Preprocessing and storing the stats...")
    preprocess_and_store_stats(data_processor, storage)

    # Preprocess and store slots from the characters data
    print("Preprocessing and storing the slots...")
    preprocess_and_store_slots(data_processor, storage)

    # Preprocess and store the characters from the characters data
    print("Preprocessing and storing the characters...")
    preprocess_and_store_characters(data_processor, storage)

    # Preprocess and store the characters stats from the characters data
    print("Preprocessing and storing the characters-stats...")
    preprocess_and_store_characters_stats(data_processor, storage)

    # Preprocess and store the characters items from the characters data
    print("Preprocessing and storing the characters-items...")
    preprocess_and_store_characters_items(data_processor, storage)

    # Write the "INSERT.sql" file
    file_name = "INSERT.sql"
    print("Writing the 'INSERT.sql' file...")
    write_insert_sql_file(file_name, version, storage)


def get_page_extractor_from_url(url):
    page_browser = browser.Browser(url)
    raw_html = page_browser.get_html_from_url()
    page_extractor = extractor.Extractor(raw_html)

    return page_extractor


def extract_and_store_types(page_extractor, storage):
    types = page_extractor.extract_types()
    storage.store_types(types)
    _print_verbosity_from_data(types)
    print(" Completed.\n\t --> Total of {} type(s)\n".format(len(types)))


def extract_and_store_paths(page_extractor, storage):
    paths = page_extractor.extract_paths()
    storage.store_paths(paths)
    _print_verbosity_from_data(paths)
    print(" Completed.\n\t --> Total of {} path(s)\n".format(len(paths)))


def extract_and_store_items(relics_extractor, ornaments_extractor, storage):
    relic_names = relics_extractor.extract_relics_or_ornaments_name()
    ornament_names = ornaments_extractor.extract_relics_or_ornaments_name()
    item_names = relic_names + ornament_names
    storage.store_items(item_names)
    _print_verbosity_from_data(relic_names, title="Relics")
    _print_verbosity_from_data(ornament_names, title="Ornaments")
    print(" Completed.\n\t --> Total of {} item(s)\n".format(len(item_names)))


def extract_and_store_items_sets(
        relics_extractor, ornaments_extractor, storage):
    relic_details = relics_extractor.extract_relics_or_ornaments_description()
    ornament_details = (
        ornaments_extractor.extract_relics_or_ornaments_description())
    item_details = relic_details + ornament_details
    storage.store_items_sets(item_details)
    print(" Completed.\n\t --> Total of {} items set(s)\n".format(
        len(item_details)))


def extract_and_store_characters_data(url, page_extractor, storage):
    characters_raw_data = page_extractor.extract_characters_data(url)
    storage.store_characters_raw_data(characters_raw_data)
    print(" Completed.\n\t --> Total of {} character(s) data\n".format(
        len(characters_raw_data)))


def preprocess_and_store_stats(data_processor, storage):
    stats = data_processor.pre_process_characters_data_for_stat()
    storage.store_stats(stats)
    _print_verbosity_from_data(stats)
    print(" Completed.\n\t --> Total of {} stat(s)\n".format(len(stats)))


def preprocess_and_store_slots(data_processor, storage):
    slots = data_processor.pre_process_characters_data_for_slot()
    storage.store_slots(slots)
    _print_verbosity_from_data(slots)
    print(" Completed.\n\t --> Total of {} slot(s)\n".format(len(slots)))


def preprocess_and_store_characters(data_processor, storage):
    characters = data_processor.pre_process_characters_data_for_character()
    storage.store_characters(characters)
    print(" Completed.\n\t --> Total of {} character(s)\n".format(
        len(characters)))


def preprocess_and_store_characters_stats(data_processor, storage):
    characters_stats = (
        data_processor.pre_process_characters_data_for_character_stat())
    storage.store_characters_stats(characters_stats)
    print(" Completed.\n\t --> Total of {} characters-stat(s)\n".format(
        len(characters_stats)))


def preprocess_and_store_characters_items(data_processor, storage):
    characters_items = (
        data_processor.pre_process_characters_data_for_character_item())
    storage.store_characters_items(characters_items)
    print(" Completed.\n\t --> Total of {} characters-item(s)\n".format(
        len(characters_items)))


def write_insert_sql_file(file_name, version, storage):
    file_writer = Writer()
    file_writer.write_insert_sql_file(file_name, version, storage)
    print(" Completed.")


def _print_verbosity_from_data(data_list, title=""):
    if title != "":
        print("  {}:".format(title))

    [print("\t> {}".format(data))for data in data_list]


if __name__ == '__main__':
    main()
