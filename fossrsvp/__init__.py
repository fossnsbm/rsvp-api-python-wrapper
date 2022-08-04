import os
import requests


class APIKeyMissingError(Exception):
    pass


session = requests.Session()
session.params = {}

from .rsvp import FossRsvp
