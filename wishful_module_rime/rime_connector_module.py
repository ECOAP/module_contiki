import wishful_framework as wishful_module
from wishful_module_contikibase.net_connector_module import NetConnectorModule


@wishful_module.build_module
class RIMEConnector(NetConnectorModule):

    def __init__(self, **kwargs):
        super(RIMEConnector, self).__init__(**kwargs)
