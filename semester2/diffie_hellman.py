from collections import namedtuple
from random import randint
from math import isqrt

Configuration = namedtuple("Configuration", "p g")
CODE_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#_"
ABSOLUTE_RANDOM_PRIME_NUMBER = 23


def random_configuration():
    prime_number = ABSOLUTE_RANDOM_PRIME_NUMBER
    return Configuration(p=prime_number, g=randint(2, 42))


def random_private_key(config: Configuration):
    return randint(isqrt(config.p), config.p - 1)


def generate_public_key(config: Configuration, private_key: int):
    return pow(config.g, private_key, config.p)


def generate_secret(config: Configuration, private_key: int, contact_key: int):
    return pow(contact_key, private_key, config.p)
