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
        types_list = self._extract_html_from_filters_divider_tag("element")

        return types_list

    def extract_paths(self):
        paths_list = self._extract_html_from_filters_divider_tag("path")

        return paths_list

    def _extract_html_from_filters_divider_tag(self, string_to_find):
        pattern = '<div class="filters-divider"></div>.*?</div></div>'
        match_results = re.search(pattern, self._raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()

        pattern = '<img alt=".*?" .*?>'
        match_results_list = re.findall(
            pattern, match_results_grouped, re.IGNORECASE)
        results_list = [line
                        for line in match_results_list
                        if line.find(string_to_find) != -1]
        results_list = [re.sub('<.*?"', '', line)
                        for line in results_list]
        results_list = [re.sub('".*?>', '', line)
                        for line in results_list]

        return results_list

    def extract_relics_or_ornaments_name(self):
        relics_or_ornaments_details_list = (
            self._extract_html_from_light_cones_item_tag())
        names_list = [re.sub('<.*?><img alt="', '', line)
                      for line in relics_or_ornaments_details_list]
        names_list = [re.sub('".*?</p></div></div></div>', '', line)
                      for line in names_list]
        names_list = [name.replace("'", "''")
                      for name in names_list]

        return names_list

    def extract_relics_or_ornaments_description(self):
        relics_or_ornaments_details_list = (
            self._extract_html_from_light_cones_item_tag())
        new_relics_or_ornaments_details_list = list()

        for line in relics_or_ornaments_details_list:
            pattern = '<div class="light-cones-set">.*?</p></div>'
            match_results = re.findall(pattern, line, re.IGNORECASE)

            name = re.sub('<.*?><img alt="', '', line)
            name = re.sub('".*?</p></div></div></div>', '', name)

            for match in match_results:
                count = re.sub(
                    '<.*?><div class="light-cones-count">', '', match)
                count = re.sub(
                    '</div>.*?</div>', '', count)

                description = re.sub(
                    '.*?<p class="light-cones-description">', '', match)
                description = re.sub(
                    '</p></div>', '', description)
                description = description.replace("'", "''")

                new_relics_or_ornaments_details_list.append(
                    (name, count, description))

        return new_relics_or_ornaments_details_list

    def _extract_html_from_light_cones_item_tag(self):
        pattern = '<div class="light-cones-item">.*?</p></div></div></div>'
        match_results_list = re.findall(pattern, self._raw_html, re.IGNORECASE)

        return match_results_list

    def extract_characters_data(self, main_page_url):
        character_hrefs_list = self._extract_html_from_character_list_tag()
        character_urls_list = [main_page_url.replace('/star-rail/', href)
                               for href in character_hrefs_list]

        characters_data_list = list()
        [characters_data_list.append(self._extract_character_data(url))
         for url in character_urls_list]

        return characters_data_list

    def _extract_html_from_character_list_tag(self):
        pattern = '<div class="character-list">.*?</a></div></main>'
        match_results = re.search(pattern, self._raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()

        pattern = '<a href=".*?">'
        match_results_list = re.findall(
            pattern, match_results_grouped, re.IGNORECASE)
        character_hrefs_list = [re.sub('<a href="', '', line)
                                for line in match_results_list]
        character_hrefs_list = [re.sub('" .*?>', '', line)
                                for line in character_hrefs_list]

        return character_hrefs_list

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
        pattern = ('<h2 class="character-info-build-section-title">.*?</div>'
                   '</div></div></div>')
        match_results_titles_list = re.findall(
            pattern, character_raw_html, re.IGNORECASE)
        match_results_titles_relics_and_ornaments_list = [
            title for title in match_results_titles_list
            if title.find("Relics") != -1]
        relics_and_ornaments_dict = dict()

        for all_relics_and_ornaments in (
                match_results_titles_relics_and_ornaments_list):
            # Title
            pattern = '<h2 .*?>.*?</h2>'
            match_results = re.search(
                pattern, all_relics_and_ornaments, re.IGNORECASE)
            match_results_grouped = match_results.group()
            relics_and_ornaments = re.sub(
                '<h2 .*?>', '', match_results_grouped)
            relics_and_ornaments = re.sub(
                '</h2>', '', relics_and_ornaments)
            relics_and_ornaments = relics_and_ornaments.split(" ")[-1].lower()
            relics_and_ornaments_list = list()

            pattern = ('<div class="character-info-weapon-rank">.*?</div>'
                       '</div></div>')
            match_results_relics_and_ornaments_list = re.findall(
                pattern, all_relics_and_ornaments, re.IGNORECASE)

            for single_relic_or_ornament in (
                    match_results_relics_and_ornaments_list):
                # Name & Quantity
                pattern = ('<div class="character-info-weapon-name">.*?</div>'
                           '</div>')
                match_results_list = re.findall(
                    pattern, single_relic_or_ornament, re.IGNORECASE)
                names_and_quantities_list = [
                    re.sub('<div class=".*?">', '', line)
                    for line in match_results_list]
                names_and_quantities_list = [
                    re.sub('</div></div>', '', line)
                    for line in names_and_quantities_list]
                names_and_quantities_list = [
                    re.sub('</div>', ';', name_and_quantity)
                    for name_and_quantity in names_and_quantities_list]
                relics_and_ornaments_list.append(names_and_quantities_list)
            relics_and_ornaments_dict[
                relics_and_ornaments] = relics_and_ornaments_list

        # Stats & Substats
        pattern = ('<h2 class="character-info-build-section-title">.*?</div>'
                   '</div></div>')
        match_results_titles_list = re.findall(
            pattern, character_raw_html, re.IGNORECASE)
        match_results_titles_stats_and_substats_list = [
            title for title in match_results_titles_list
            if title.find("stats") != -1]
        stats_and_substats_dict = dict()

        for all_stats_and_substats in (
                match_results_titles_stats_and_substats_list):
            # Title
            pattern = '<h2 .*?>.*?</h2>'
            match_results = re.search(
                pattern, all_stats_and_substats, re.IGNORECASE)
            match_results_grouped = match_results.group()
            stats_and_substats = re.sub(
                '<h2 .*?>', '', match_results_grouped)
            stats_and_substats = re.sub(
                '</h2>', '', stats_and_substats)
            stats_and_substats = stats_and_substats.split(" ")[-1].lower()
            stats_and_substats_list = list()

            pattern = '<div class="character-info-stats-item">.*?</div>'
            match_results_stats_and_substats_list = re.findall(
                pattern, all_stats_and_substats, re.IGNORECASE)

            for single_stat_or_substat in (
                    match_results_stats_and_substats_list):
                if single_stat_or_substat.find("<b>") != -1:
                    slot_and_stat = re.sub(
                        '<div .*?><b>', '', single_stat_or_substat)
                    slot_and_stat = re.sub(
                        '</b>', '', slot_and_stat)
                    slot_and_stat = re.sub(
                        '</div>', '', slot_and_stat)
                    slot_and_stat = slot_and_stat.replace(": ", ";")
                    stats_and_substats_list.append(slot_and_stat)
                else:
                    substat = re.sub('<div .*?>', '', single_stat_or_substat)
                    substat = re.sub('</div>', '', substat)
                    stats_and_substats_list.append(substat)

            stats_and_substats_dict[
                stats_and_substats] = stats_and_substats_list

        relics_and_ornaments_dict_keys = [
            key for key in relics_and_ornaments_dict.keys()]
        stats_and_substats_dict_keys = [
            key for key in stats_and_substats_dict.keys()]
        character_data = {
            "name": name,
            "rarity": rarity,
            "type": type,
            "path": path,
            relics_and_ornaments_dict_keys[0]: relics_and_ornaments_dict[
                relics_and_ornaments_dict_keys[0]],
            relics_and_ornaments_dict_keys[1]: relics_and_ornaments_dict[
                relics_and_ornaments_dict_keys[1]],
            stats_and_substats_dict_keys[0]: stats_and_substats_dict[
                stats_and_substats_dict_keys[0]],
            stats_and_substats_dict_keys[1]: stats_and_substats_dict[
                stats_and_substats_dict_keys[1]]}

        return character_data
