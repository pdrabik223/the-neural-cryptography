import unittest
from __init__ import (pad, unpad, encrypt_aes, decrypt_aes,
                      encrypt_des, decrypt_des)


class TestCrypto(unittest.TestCase):
    def test_pad_unpad(self):
        text = 'Hello world'
        padded = pad(text, 8)
        self.assertEqual(text, unpad(padded),
                         'Padded and unpaded text is not the same')

    def test_aes_encrypt_decrypt(self):
        msg, pssd = 'Hello world', 'pssd'
        encrypted = encrypt_aes(msg, pssd)
        decrypted = decrypt_aes(encrypted, pssd)
        self.assertEqual(msg, decrypted.decode('utf-8'),
                         'Decrypted and encrypted text is not the same')

    def test_des_encrypt_decrypt(self):
        msg, pssd = 'Hello world', '12345678'
        encrypted = encrypt_des(msg, pssd)
        decrypted = decrypt_des(encrypted, pssd)
        self.assertEqual(msg, decrypted.decode('utf-8'),
                         'Decrypted and encrypted text is not the same')


if __name__ == '__main__':
    unittest.main()
