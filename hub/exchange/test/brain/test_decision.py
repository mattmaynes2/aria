from unittest import TestCase
from brain.strategies.decision import Decision
from ipc import Message

class TestDecision(TestCase):

    def test_equal(self):
        message= Message()
        d1 = Decision(message,1)
        d2 = Decision(message,1)
        d3 = Decision(message,2)
        self.assertTrue(d1 == d2)
        self.assertFalse(d1 == d3)
