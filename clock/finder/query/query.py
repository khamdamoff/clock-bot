import copy

from clock.finder.query.params import QUERY_PARAM_LANG


class SearchQuery:
    def __init__(self, query_lower: str, params: dict):
        self.query_lower = query_lower
        self.params = params

    @property
    def lang(self):
        return self.get_param(QUERY_PARAM_LANG)

    def get_param(self, param: str):
        return self.params.get(param)

    def is_empty(self):
        return not self.query_lower

    def copy(self):
        return copy.copy(self)
