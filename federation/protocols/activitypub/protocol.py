import logging

from federation.protocols.base import BaseProtocol

PROTOCOL_NAME = "activitypub"


def identify_payload(payload):
    """Each protocol module should define an `identify_payload` method.

    Args:
        payload (str)   - Payload blob

    Returns:
        True or False   - A boolean whether the payload matches this protocol.
    """
    raise NotImplementedError("Implement in protocol module")


class Protocol(BaseProtocol):

    logger = logging.getLogger("federation")

    def build_send(self, entity, from_user, to_user=None):
        obj = entity.to_as2()

    def receive(self, payload, user=None, sender_key_fetcher=None, *args, **kwargs):
        pass
