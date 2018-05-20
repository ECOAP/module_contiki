import wishful_framework as wishful_module
import wishful_upis as upis
from wishful_module_contikibase.net_connector_module import NetConnectorModule
import traceback
import sys


@wishful_module.build_module
class IPv6Connector(NetConnectorModule):

    def __init__(self, **kwargs):
        super(IPv6Connector, self).__init__(**kwargs)

    @wishful_module.bind_function(upis.net.rpl_set_border_router)
    def rpl_set_border_router(self, rpl_prefix):
        node = self.node_factory.get_node(self.interface)
        print(rpl_prefix)
        try:
            return node.forward_rpc("rpl_connector", "rpl_set_border_router", rpl_prefix)
        except:
            traceback.print_exc(file=sys.stdout)

    @wishful_module.bind_function(upis.net.add_route)
    def ipv6_route_add(self, dest_ipv6_addr, num_hops, nexthop_ipv6_addr):
        node = self.node_factory.get_node(self.interface)
        try:
            return node.forward_rpc("ipv6_connector", "add_route", dest_ipv6_addr, nexthop_ipv6_addr, num_hops)
        except:
            traceback.print_exc(file=sys.stdout)

    @wishful_module.bind_function(upis.net.add_neighbor)
    def nd6_add_neighbor(self, neighbor_ipv6_addr, neighbor_mac_addr, is_router):
        node = self.node_factory.get_node(self.interface)
        try:
            return node.forward_rpc("ipv6_connector", "add_neighbor", neighbor_ipv6_addr, neighbor_mac_addr, is_router)
        except:
            traceback.print_exc(file=sys.stdout)


    @wishful_module.bind_function(upis.net.clear_route_table)
    def clear_route_table(self):
        node = self.node_factory.get_node(self.interface)
        try:
            return node.forward_rpc("ipv6_connector", "clear_route_table")
        except:
            traceback.print_exc(file=sys.stdout)
