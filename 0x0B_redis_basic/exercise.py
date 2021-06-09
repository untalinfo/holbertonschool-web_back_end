#!/usr/bin/env python3
"""
exercises module
"""
import redis
from typing import Union, Callable, List, Optional
import uuid
import sys
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Count amount of calls to method
    """
    k = method.__qualname__

    @wraps(method)
    def counter_wrapper(self, *args, **kwargs):
        """
        Wrapper for method
        """
        self._redis.incr(k)
        return method(self, *args, **kwargs)
    return counter_wrapper


def call_history(method: Callable) -> Callable:
    """
    Store history of inputs and outputs for a function
    """
    i_keys = method.__qualname__ + ":inputs"
    o_keys = method.__qualname__ + ":outputs"

    @wraps(method)
    def set_history(self, *args, **kwargs):
        """
        Set list keys to wrapped function
        """
        self._redis.rpush(i_keys, str(args))
        r = method(self, *args, **kwargs)
        self._redis.rpush(o_keys, str(r))
        return r

    return set_history


def replay(method: Callable) -> None:
    """
    Ouput log of actions taken on method
    """
    counter_key = method.__qualname__
    i_keys = method.__qualname__ + ':inputs'
    o_keys = method.__qualname__ + ':outputs'
    this = method.__self__

    counter = this.get_str(counter_key)
    history = list(zip(this.get_list(i_keys),
                       this.get_list(o_keys)))
    print("{} was called {} times:".format(counter_key, counter))
    for call in history:
        v = this.get_str(call[0])
        k = this.get_str(call[1])
        print("{}(*{}) -> {}".format(counter_key, v, k))


class Cache:
    """ Cache class
    """
    def __init__(self):
        """
        Instantiate a empty Redis
        """
        self._redis = redis.Redis(host="localhost", port=6379)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store any type of data in Redis
        """
        k = str(uuid.uuid4())
        self._redis[k] = data
        return k

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """
        Get value in db with callback format
        """
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(self, b: bytes) -> str:
        """
        bytes to str
        """
        return b.decode('utf-8')

    def get_int(self, b: bytes) -> int:
        """
        bytes to int
        """
        return int.from_bytes(b, sys.byteorder)

    def get_list(self, k: str) -> List:
        """
        bytes from store to list
        """
        return self._redis.lrange(k, 0, -1)
