from unittest import TestCase

import exchange

class ExchangeTest (TestCase):

    def setUp (self):
        self.exchange = exchange.Exchange()

    def test_hello (self):
        self.assertEquals('hello', 'hello')


