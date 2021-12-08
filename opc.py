import socket
import sys
sys.path.insert(0, "..")
import logging

from opcua import Client, ua


class SubHandler(object):
    """
    Client to subscription. It will receive events from server
    """

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event)

class OPC:
    def __init__(self, url):
        logging.basicConfig(level=logging.WARN)
        try:
            self.client = Client(url)
            self.client.connect()
        except socket.timeout as e:
            print(e)

    def add_node(self, node):

        self.node = self.client.get_node(node)

    def send(self, value):
        try:
            dv = ua.DataValue(ua.Variant(value, ua.VariantType.Double))
            dv.ServerTimestamp = None
            dv.SourceTimestamp = None
            print(value)
            self.node.set_value(dv)
        except AttributeError as e:
            print(e)

    def create_subscribtion(self):
        handler = SubHandler()
        self.sub = self.client.create_subscription(500, handler)
        self.handle = self.sub.subscribe_data_change(self.node)

    def delete_subscribtion(self, ):
        self.sub.unsubscribe(self.handle)
        self.sub.delete()

    def disconnect(self):
        self.client.disconnect()