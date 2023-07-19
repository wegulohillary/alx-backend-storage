#!/usr/bin/env python3
""" Redis Module """

import requests
import time
from functools import wraps

def count_requests(func):
    @wraps(func)
    def wrapper(url):
        count_key = f"count:{url}"
        count = int(redis.get(count_key) or 0)
        count += 1
        redis.set(count_key, count, ex=10)
        return func(url)
    return wrapper

@count_requests
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text
