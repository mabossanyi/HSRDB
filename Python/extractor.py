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
        list_types = self._extract_html_from_filters("element")

        return list_types

    def extract_paths(self):
        list_paths = self._extract_html_from_filters("path")

        return list_paths

    def _extract_html_from_filters(self, string_to_find):
        pattern = '<div class="filters-divider"></div>.*?</div></div>'
        match_results = re.search(pattern, self._raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()

        pattern = '<img alt=".*?" .*?>'
        match_results_list = re.findall(pattern, match_results_grouped, re.IGNORECASE)
        list_html = [line for line in match_results_list if line.find(string_to_find) != -1]
        list_html = [re.sub('<.*?"', '', s) for s in list_html]
        list_html = [re.sub('".*?>', '', s) for s in list_html]

        return list_html

    def extract_relics_or_ornaments(self):
        pattern = '<div class="light-cones-item">.*?</div>'
        match_results_list = re.findall(pattern, self._raw_html, re.IGNORECASE)
        list_html = [re.sub('<.*?><img alt="', '', s) for s in match_results_list]
        list_html = [re.sub('".*?</div>', '', s) for s in list_html]

        return list_html


