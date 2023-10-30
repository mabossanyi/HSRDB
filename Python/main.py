# Libraries
import browser
import extractor
import storage
import writer


if __name__ == '__main__':
    # Extract the HTML from the webpage for the types and the paths
    main_page_url = "https://genshin.gg/star-rail/"
    main_page_browser = browser.Browser(main_page_url)
    raw_html = main_page_browser.get_html_from_url()

    # Get the classes "Extractor", "Storage" and "Writer"
    main_page_extractor = extractor.Extractor(raw_html)
    storage = storage.Storage()
    writer = writer.Writer()

    # Extract the types
    types = main_page_extractor.extract_types()

    # Store the types
    storage.store_types(types)

    # Write the "INSERT_TYPE.sql" file
    writer.write_insert_type_sql_file("INSERT_TYPE.sql", storage)

    # Extract the path
    paths = main_page_extractor.extract_paths()

    # Store the paths
    storage.store_paths(paths)

    # Write the "INSERT_PATH.sql" file
    writer.write_insert_path_sql_file("INSERT_PATH.sql", storage)

    # Extract the HTML from the webpage for the relics and the ornaments
    relics_page_url = "https://genshin.gg/star-rail/relics/"
    relics_page_browser = browser.Browser(relics_page_url)
    raw_html_relics = relics_page_browser.get_html_from_url()

    ornaments_page_url = "https://genshin.gg/star-rail/planar-ornaments/"
    ornaments_page_browser = browser.Browser(ornaments_page_url)
    raw_html_ornaments = ornaments_page_browser.get_html_from_url()

    # Get the class "Extractor"
    relics_page_extractor = extractor.Extractor(raw_html_relics)
    ornaments_page_extractor = extractor.Extractor(raw_html_ornaments)

    # Extract the relic names and ornament names
    relic_names = relics_page_extractor.extract_relics_or_ornaments_name()
    ornament_names = ornaments_page_extractor.extract_relics_or_ornaments_name()
    relic_ornament_names = relic_names + ornament_names

    # Store the items
    storage.store_items(relic_ornament_names)

    # Write the "INSERT_ITEM.sql" file
    writer.write_insert_item_sql_file("INSERT_ITEM.sql", storage)

    # Extract the relic set description and ornament set description
    relic_details = relics_page_extractor.extract_relics_or_ornaments_description()
    ornament_details = ornaments_page_extractor.extract_relics_or_ornaments_description()
    relic_ornament_details = relic_details + ornament_details

    # Store the items sets
    storage.store_items_sets(relic_ornament_details)

    # Write the "INSERT_ITEMS_SET.sql" file
    writer.write_insert_items_set_sql_file("INSERT_ITEMS_SET.sql", storage)

    # Extract the characters data for each character on the main page
    characters_data = main_page_extractor.extract_characters_data(main_page_url)

    # Store the characters data
    storage.store_characters_raw_data(characters_data)
