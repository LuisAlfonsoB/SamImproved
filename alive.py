from time import sleep
from requests import get as zget
from os import environ
from logging import error as logerror

BASE_URL = environ.get('QB_BASE_URL', None)
try:
    if len(QB_BASE_URL) == 0:
        raise TypeError
    QB_BASE_URL = QB_BASE_URL.rstrip("/")
except TypeError:
    QB_BASE_URL = None
PORT = environ.get('PORT', None)
if PORT is not None and QB_BASE_URL is not None:
    while True:
        try:
            zget(QB_BASE_URL).status_code
            sleep(90)
        except Exception as e:
            logerror(f"alive.py: {e}")
            sleep(2)
            continue
