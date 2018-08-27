import unittest

from run_length_encoding import *

from hypothesis import given, example
from hypothesis.strategies import text

class Test_RunLengthEncoding(unittest.TestCase):
    @given(s=text())
    @example(s='')
    def test_decode_inverts_encode(self, s):
        self.assertEqual(decode(encode(s)), s)

if __name__ == '__main__':
    unittest.main()




