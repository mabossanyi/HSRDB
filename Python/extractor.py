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
        pattern = '<div class="filters-divider"></div>.*?<div class="filters-divider"></div>'
        match_results = re.search(pattern, self._raw_html, re.IGNORECASE)
        raw_types_html = match_results.group()

        pattern = '<img alt=".*?" .*?>'
        match_results = re.findall(pattern, raw_types_html, re.IGNORECASE)
        list_types_html = match_results
        list_types = [re.sub('<.*?"', '', s) for s in list_types_html]
        list_types = [re.sub('".*?>', '', s) for s in list_types]

        return list_types