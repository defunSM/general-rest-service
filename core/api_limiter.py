""" Limits  the number of API calls that can be made """

from functools import wraps
from fastapi import HTTPException, status
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


def limit_api_calls(func):
    """ Decorator that restricts the number of API calls per minute by using the client's IP."""
    @wraps(func)
    def wrapper(*args, **kwargs):

        client_ip = kwargs.get('_request').client.host
        res = limiter(client_ip, 5)

        if res['call']:
            return func(*args, **kwargs)

        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail={ "message": "call limit reached",
                                     "ttl": res["ttl"]})

    return wrapper
