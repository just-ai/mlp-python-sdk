import os

from graypy import GELFUDPHandler


class GrayLogHandler(GELFUDPHandler):

    def _make_gelf_dict(self, record):
        data_dict = super()._make_gelf_dict(record)

        data_dict['graylog_env'] = os.environ.get('GRAYLOG_ENV')
        data_dict['mlp_account_id'] = os.environ.get('MLP_ACCOUNT_ID')
        data_dict['mlp_model_id'] = os.environ.get('MLP_MODEL_ID')

        return data_dict
