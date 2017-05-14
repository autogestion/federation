def get_outbound_entity(entity, private_key):
    """Get the correct outbound entity for this protocol.

    We might have to look at entity values to decide the correct outbound entity.
    If we cannot find one, we should raise as conversion cannot be guaranteed to the given protocol.

    Private key of author is needed to be passed for signing the outbound entity.

    :arg entity: An entity instance which can be of a base or protocol entity class.
    :returns: Protocol specific entity class instance.
    :raises ValueError: If conversion cannot be done.
    """
    outbound = None
    cls = entity.__class__
    if cls in [DiasporaPost, DiasporaRequest, DiasporaComment, DiasporaLike, DiasporaProfile, DiasporaRetraction]:
        # Already fine
        outbound = entity
    elif cls == Post:
        outbound = DiasporaPost.from_base(entity)
    elif cls == Comment:
        outbound = DiasporaComment.from_base(entity)
    elif cls == Reaction:
        if entity.reaction == "like":
            outbound = DiasporaLike.from_base(entity)
    elif cls == Relationship:
        if entity.relationship in ["sharing", "following"]:
            # Unfortunately we must send out in both cases since in Diaspora they are the same thing
            outbound = DiasporaRequest.from_base(entity)
    elif cls == Profile:
        outbound = DiasporaProfile.from_base(entity)
    elif cls == Retraction:
        outbound = DiasporaRetraction.from_base(entity)
    if not outbound:
        raise ValueError("Don't know how to convert this base entity to Diaspora protocol entities.")
    if isinstance(outbound, DiasporaRelayableMixin) and not outbound.signature:
        # Sign by author if not signed yet. We don't want to overwrite any existing signature in the case
        # that this is being sent by the parent author
        outbound.sign(private_key)
        # If missing, also add same signature to `parent_author_signature`. This is required at the moment
        # in all situations but is apparently being removed.
        # TODO: remove this once Diaspora removes the extra signature
        outbound.parent_signature = outbound.signature
    return outbound
