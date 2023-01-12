from graypy import GELFUDPHandler


class GrayLogHandler(GELFUDPHandler):

    def _make_gelf_dict(self, record):
        data_dict = super()._make_gelf_dict(record)
        # TODO use your fields, specify in __init__ if needed
        return data_dict
