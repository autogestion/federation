import logging

# Should be implemented by submodules
PROTOCOL_NAME = None


def identify_payload(payload):
    """Each protocol module should define an `identify_payload` method.

    Args:
        payload (str)   - Payload blob

    Returns:
        True or False   - A boolean whether the payload matches this protocol.
    """
    raise NotImplementedError("Implement in protocol module")


class BaseProtocol():

    logger = logging.getLogger("federation")

    def build_send(self, *args, **kwargs):
        """Build a payload for sending.

        Args:
            entity (obj)            - Entity to send
            from_user (obj)         - The user object who is sending
                                      Must contain attributes `handle` and `private_key`
            to_user (obj, optional) - The user object we are sending to
                                      Must contain attribute `key` (public key)
        """
        raise NotImplementedError("Implement in subclass")

    def receive(self, payload, user=None, sender_key_fetcher=None, *args, **kwargs):
        """Receive a payload.

        Args:
            payload (str)                           - Payload blob
            user (optional, obj)                    - Target user object
                                                      If given, MUST contain `key` attribute which corresponds to user
                                                      decrypted private key
            sender_key_fetcher (optional, func)     - Function that accepts sender handle and returns public key

        Returns tuple of:
            str - Sender handle ie user@domain.tld
            str - Extracted message body
        """
        raise NotImplementedError("Implement in subclass")
