import vcr
from unittest import TestCase
from pykanyerest.quotes import *


class TestGetNewQuote(TestCase):
    """
    Test Case for get_new_quote function from kanye.rest
    """

    @vcr.use_cassette(cassette_library_dir='./test_pykanyerest/fixtures/cassettes')
    def test_GetNewQuote(self):
        """
        """
        quote = get_new_quote()
        self.assertEqual(type(quote), dict)
        self.assertEqual(len(quote), 1)
        keys = quote.keys()
        self.assertIn('quote', keys)
        self.assertEqual(type(quote['quote']), str)
        self.assertEqual(quote['quote'], "I'm a creative genius")
