# Libraries
import re


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

                new_list_relics_or_ornaments_details.append((name, count, description))

        return new_list_relics_or_ornaments_details

    def _extract_html_from_light_cones_item_tag(self):
        pattern = '<div class="light-cones-item">.*?</p></div></div></div>'
        match_results_list = re.findall(pattern, self._raw_html, re.IGNORECASE)

        return match_results_list
