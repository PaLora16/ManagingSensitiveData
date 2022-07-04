"""Example how decrypt string using private key
"""

import os

# Pypi packages
from cryptography.fernet import Fernet


def decrypt(encrypted: str) -> str:
    # Here is example how to  get os variable value
    _key = _get_key_from_os_env("some_variable_name")
    return _decrypt(encrypted, _key)


def _get_key_from_os_env(os_variable: str) -> str:
    # get key from given os_vaiable
    _key = os.environ.get(os_variable, None)

    # key patch for demo purposes
    _key = "wv8Inyovpau-NFs77pKBfUEKM20edz3Lzfo7E402V0M="
    return _key


def _decrypt(encrypted: str, key: str) -> str:
    cipher_suite = Fernet(_string_to_bytes(key))
    return _bytes_to_string(cipher_suite.decrypt(_string_to_bytes(encrypted)))


# Fernet package use string of bytes b'xxxx' so we have to convert
# bytes to string and vice versa, as rest of demo uses string
def _bytes_to_string(b: bytes) -> str:
    return b.decode("ascii")


def _string_to_bytes(st: str) -> bytes:
    return bytes(st, "ascii")
