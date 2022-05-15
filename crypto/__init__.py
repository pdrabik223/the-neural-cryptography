'''
Utility library for cryptographic functions
'''


import base64
import hashlib

import matplotlib.pyplot as plt
import numpy as np

from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto import Random

# Instance of a random number generator used to create input vectors
_rng = Random.new()


def pad(s: str, block_size) -> str:
    '''
    Padds the str to given block size
    '''
    return s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)


def unpad(s: str) -> str:
    '''
    Removes the padding from the str
    '''
    return s[:-ord(s[len(s) - 1:])]


def sha256(s: str) -> bytes:
    '''
    Calculate sha256 hash of str
    '''
    return hashlib.sha256(s.encode('utf-8')).digest()  # digest?


def encrypt_aes(text: str, key: str,
                input_vector: bytes = None) -> bytes:
    '''
    Encrypt str using AES algorithm (Key is being hashed using SHA256)
    If input_vector is None (default) random bytes will be generated
    '''
    if input_vector is None:
        input_vector = _rng.read(AES.block_size)
    assert len(
        input_vector) == AES.block_size, 'Input vector needs to have the same len as block size'

    key = sha256(key)

    text = pad(text, AES.block_size).encode('utf-8')

    # XXX: Block size needs to be 16 bytes
    # XXX: Private key can be only 16, 128 or 256 bytes
    cipher = AES.new(key, AES.MODE_CBC, input_vector)

    # Base64 encode to avoid problems with printing
    return input_vector + cipher.encrypt(text)


def decrypt_aes(secret: bytes, key: str) -> bytes:
    '''
    Decrypt bytes using AES algorithm (Key is assumed to be hashed using SHA256)
    '''
    private_key = sha256(key)

    # First block contains the seed
    input_vector = secret[:AES.block_size]
    cipher = AES.new(private_key, AES.MODE_CBC, input_vector)
    return unpad(cipher.decrypt(secret[AES.block_size:]))


def encrypt_des(text: str, key: str,
                input_vector: bytes = None) -> bytes:
    '''
    Encrypt str using DES algorithm (key needs to be exactly 8 bytes long).
    If input_vector is None (default) random bytes will be generated
    '''

    assert len(key) == 8, 'Key needs to be 8 bytes long'

    if input_vector is None:
        input_vector = _rng.read(DES.block_size)
    assert len(
        input_vector) == DES.block_size, 'Input vector needs to have the same len as block size'
    text = text.encode('utf-8')

    key = key.encode('utf-8')
    cipher = DES.new(key, DES.MODE_OFB, input_vector)
    encrypted = input_vector + cipher.encrypt(text)
    return encrypted


def decrypt_des(secret: bytes, key: str) -> bytes:
    '''
    Decrypt bytes using DES algorithm
    '''
    input_vector = secret[:DES.block_size]
    cipher = DES.new(key.encode('utf-8'), DES.MODE_OFB, input_vector)
    decrypted = cipher.decrypt(secret[DES.block_size:])
    return decrypted
