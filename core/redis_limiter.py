""" Redis file for limiting API Calls to fastapi backend"""

import redis

client = redis.Redis(host="redis-server")

def limiter(key, limit):
    """ Returns weither the call can be made (bool) and the time

    Args:
        key (_type_): _description_
        limit (_type_): _description_

    Returns:
        _type_: _description_
    """
    req = client.incr(key)

    if req == 1:
        client.expire(key, 60)
        ttl = 60
    else:
        ttl = client.ttl(key)

    if req > limit:
        return {
            "call": False,
            "ttl": ttl
        }

    return {
        "call": True,
        "ttl": ttl
    }
