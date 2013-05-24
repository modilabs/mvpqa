import os
import json

from jinja2 import Template
from jinja2 import Environment

from pybamboo.connection import Connection
from pybamboo.dataset import Dataset

from mvpqa.periods import datetimeformat

BAMBOO_URL = "http://localhost:8080"

# load custom dateformat to be used by templates
env = Environment()
env.filters['datetimeformat'] = datetimeformat


class BambooIndicator(object):
    def __init__(self):
        self.connection = Connection(BAMBOO_URL)
        self._set_sources()

    def _set_sources(self):
        path = os.path.join(
            os.path.dirname(__file__), 'sources.json'
        )
        f = open(path)
        self._sources_dict = json.loads(f.read())
        self._sources = self._sources_dict['sources']

    def _calculation_exists(self, name, dataset):
        calculations = dataset.get_calculations()
        if 'error' in calculations:
            raise Exception(calculations['error'])
        for calc in calculations:
            if isinstance(calc, dict) and calc['name'] == name:
                return True
        return False

    def get_indicator_value(self, indicator, period):
        assert 'value' in indicator
        assert isinstance(indicator, dict)
        value = indicator['value']
        if 'sum' in value:
            sum_value = 0
            for v in value['sum']:
                dataset_id = v['dataset_id']
                # dataset_id form sources.json is most recent
                if dataset_id != self._sources[v['source']]\
                        and self._sources[v['source']] != "":
                    dataset_id = self._sources[v['source']]
                dataset = Dataset(
                    dataset_id=dataset_id, connection=self.connection)
                if 'calculation' in v:
                    # check or create calculations
                    if isinstance(v['calculation'], list):
                        for calculation in v['calculation']:
                            calc_exists = self._calculation_exists(
                                calculation.name, dataset)
                            if not calc_exists:
                                dataset.add_calculation(
                                    name=calculation['name'],
                                    formula=calculation['formula'])
                    if isinstance(v['calculation'], dict):
                        if not self._calculation_exists(
                                v['calculation']['name'], dataset):
                            calculation = v['calculation']
                            dataset.add_calculation(
                                name=calculation['name'],
                                formula=calculation['formula'])
                if 'query' in v:
                    query_string = json.dumps(v['query'])
                    template = Template(query_string)
                    query_string = template.render(period=period)
                    v['query'] = json.loads(query_string)
                if 'count' in v and 'query' in v:
                    sum_value += dataset.get_data(
                        query=v['query'], count=v['count'])
            return sum_value
