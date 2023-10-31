# Libraries
import re

import browser


class Extractor:
    # Attributes
    _raw_html = ''

    # Constructors
    def __init__(self, raw_html):
        self._raw_html = raw_html

    # Methods
    def extract_types(self):
        list_types = self._extract_html_from_filters_divider_tag("element")

        return list_types

    def extract_paths(self):
        list_paths = self._extract_html_from_filters_divider_tag("path")

        return list_paths

    def _extract_html_from_filters_divider_tag(self, string_to_find):
        pattern = '<div class="filters-divider"></div>.*?</div></div>'
        match_results = re.search(pattern, self._raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()

        pattern = '<img alt=".*?" .*?>'
        match_results_list = re.findall(pattern, match_results_grouped, re.IGNORECASE)
        list_results = [line for line in match_results_list if line.find(string_to_find) != -1]
        list_results = [re.sub('<.*?"', '', s) for s in list_results]
        list_results = [re.sub('".*?>', '', s) for s in list_results]

        return list_results

    def extract_relics_or_ornaments_name(self):
        list_relics_or_ornaments_details = self._extract_html_from_light_cones_item_tag()
        list_names = [re.sub('<.*?><img alt="', '', s) for s in list_relics_or_ornaments_details]
        list_names = [re.sub('".*?</p></div></div></div>', '', s) for s in list_names]
        list_names = [n.replace("'", "''") for n in list_names]

        return list_names

    def extract_relics_or_ornaments_description(self):
        list_relics_or_ornaments_details = self._extract_html_from_light_cones_item_tag()
        new_list_relics_or_ornaments_details = list()

        for line in list_relics_or_ornaments_details:
            pattern = '<div class="light-cones-set">.*?</p></div>'
            match_results = re.findall(pattern, line, re.IGNORECASE)

            name = re.sub('<.*?><img alt="', '', line)
            name = re.sub('".*?</p></div></div></div>', '', name)

            for match in match_results:
                count = re.sub('<.*?><div class="light-cones-count">', '', match)
                count = re.sub('</div>.*?</div>', '', count)

                description = re.sub('.*?<p class="light-cones-description">', '', match)
                description = re.sub('</p></div>', '', description)
                description = description.replace("'", "''")

                new_list_relics_or_ornaments_details.append((name, count, description))

        return new_list_relics_or_ornaments_details

    def _extract_html_from_light_cones_item_tag(self):
        pattern = '<div class="light-cones-item">.*?</p></div></div></div>'
        match_results_list = re.findall(pattern, self._raw_html, re.IGNORECASE)

        return match_results_list

    def extract_characters_data(self, main_page_url):
        list_href_characters = self._extract_html_from_character_list_tag()

        list_character_urls = [main_page_url.replace('/star-rail/', s) for s in list_href_characters]

        characters_data_list = list()
        [characters_data_list.append(self._extract_character_data(u)) for u in list_character_urls]

        return characters_data_list

    def _extract_html_from_character_list_tag(self):
        pattern = '<div class="character-list">.*?</a></div></main>'
        match_results = re.search(pattern, self._raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()

        pattern = '<a href=".*?">'
        match_results_list = re.findall(pattern, match_results_grouped, re.IGNORECASE)
        list_href_characters = [re.sub('<a href="', '', s) for s in match_results_list]
        list_href_characters = [re.sub('" .*?>', '', s) for s in list_href_characters]

        return list_href_characters

    def _extract_character_data(self, character_url):
        character_browser = browser.Browser(character_url)
        character_raw_html = character_browser.get_html_from_url()

        # Rarity
        pattern = '<img class="character-info-portrait .*?"'
        match_results = re.search(pattern, character_raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()
        rarity = re.sub('<.*? rarity-', '', match_results_grouped)
        rarity = re.sub('"', '', rarity)

        # Name
        pattern = '<img class="character-info-portrait .*? alt=".*?">'
        match_results = re.search(pattern, character_raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()
        name = re.sub('<.*? alt="', '', match_results_grouped)
        name = re.sub('">', '', name)
        name = name.replace("'", "''")

        # Type
        pattern = '<img class="character-info-element" .*?</div>'
        match_results = re.search(pattern, character_raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()
        type = re.sub('<.*? alt="', '', match_results_grouped)
        type = re.sub('"></div>', '', type)
        type = type.replace("'", "''")

        # Path
        pattern = '<img class="character-info-path-icon" .*?>.*?</div>'
        match_results = re.search(pattern, character_raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()
        path = re.sub('<.*?>', '', match_results_grouped)
        path = re.sub('</div>', '', path)
        path = path.replace("'", "''")

        # Relics & Ornaments
        pattern = '<h2 class="character-info-build-section-title">.*?</div></div></div></div>'
        match_results_titles_list = re.findall(pattern, character_raw_html, re.IGNORECASE)
        match_results_titles_relics_ornaments_list = [mr for mr in match_results_titles_list if mr.find("Relics") != -1]
        relics_and_ornaments_dict = dict()

        for all_ro_data in match_results_titles_relics_ornaments_list:
            # Title
            pattern = '<h2 .*?>.*?</h2>'
            match_results = re.search(pattern, all_ro_data, re.IGNORECASE)
            match_results_grouped = match_results.group()
            relics_and_ornaments = re.sub('<h2 .*?>', '', match_results_grouped)
            relics_and_ornaments = re.sub('</h2>', '', relics_and_ornaments)
            relics_and_ornaments = relics_and_ornaments.split(" ")[-1].lower()
            relics_and_ornaments_list = list()

            pattern = '<div class="character-info-weapon-rank">.*?</div></div></div>'
            match_results_ro_list = re.findall(pattern, all_ro_data, re.IGNORECASE)

            for single_ro_data in match_results_ro_list:
                # Name & Quantity
                pattern = '<div class="character-info-weapon-name">.*?</div></div>'
                match_results_list = re.findall(pattern, single_ro_data, re.IGNORECASE)
                names_quantities_list = [re.sub('<div class=".*?">', '', s) for s in match_results_list]
                names_quantities_list = [re.sub('</div></div>', '', s) for s in names_quantities_list]
                names_quantities_list = [re.sub('</div>', ';', s) for s in names_quantities_list]
                relics_and_ornaments_list.append(names_quantities_list)
            relics_and_ornaments_dict[relics_and_ornaments] = relics_and_ornaments_list

        # Stats & Substats (SS)
        pattern = '<h2 class="character-info-build-section-title">.*?</div></div></div>'
        match_results_titles_list = re.findall(pattern, character_raw_html, re.IGNORECASE)
        match_results_titles_stats_substats_list = [mr for mr in match_results_titles_list if mr.find("stats") != -1]
        ss_dict = dict()

        for all_ss_data in match_results_titles_stats_substats_list:
            # Title
            pattern = '<h2 .*?>.*?</h2>'
            match_results = re.search(pattern, all_ss_data, re.IGNORECASE)
            match_results_grouped = match_results.group()
            ss = re.sub('<h2 .*?>', '', match_results_grouped)
            ss = re.sub('</h2>', '', ss)
            ss = ss.split(" ")[-1].lower()
            ss_list = list()

            pattern = '<div class="character-info-stats-item">.*?</div>'
            match_results_ss_list = re.findall(pattern, all_ss_data, re.IGNORECASE)

            for single_ss_data in match_results_ss_list:
                if single_ss_data.find("<b>") != -1:
                    slot_and_stat = re.sub('<div .*?><b>', '', single_ss_data)
                    slot_and_stat = re.sub('</b>', '', slot_and_stat)
                    slot_and_stat = re.sub('</div>', '', slot_and_stat)
                    slot_and_stat = slot_and_stat.replace(": ", ";")
                    ss_list.append(slot_and_stat)
                else:
                    substat = re.sub('<div .*?>', '', single_ss_data)
                    substat = re.sub('</div>', '', substat)
                    ss_list.append(substat)

            ss_dict[ss] = ss_list

        ro_dict_keys = [key for key in relics_and_ornaments_dict.keys()]
        ss_dict_keys = [key for key in ss_dict.keys()]
        character_data = {"name": name, "rarity": rarity, "type": type, "path": path, ro_dict_keys[0]: relics_and_ornaments_dict[ro_dict_keys[0]],
                          ro_dict_keys[1]: relics_and_ornaments_dict[ro_dict_keys[1]], ss_dict_keys[0]: ss_dict[ss_dict_keys[0]],
                          ss_dict_keys[1]: ss_dict[ss_dict_keys[1]]}

        return character_data
