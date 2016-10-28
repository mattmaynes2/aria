from unittest import TestCase

import exchange

class ExchangeTest (TestCase):

    def setUp (self):
        self.exchange = exchange.Exchange()

    def test_bind (self):
        self.assertTrue(self.exchange.bind())


