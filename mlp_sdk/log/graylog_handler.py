import os

from graypy import GELFUDPHandler


class GrayLogHandler(GELFUDPHandler):

    def _make_gelf_dict(self, record):
        data_dict = super()._make_gelf_dict(record)

        data_dict['env'] = os.environ.get('GRAYLOG_ENV')
        data_dict['accountId'] = os.environ.get('MLP_ACCOUNT_ID')
        data_dict['app'] = os.environ.get('MLP_MODEL_NAME')

        return data_dict
