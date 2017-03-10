from ipc import Message
from unittest import TestCase
from brain.strategies.decision import Decision
from brain.strategies.decision_table import TableRow

class TestTableRow(TestCase):

    def test_addDecision(self):
        message= Message()
        d1 = Decision(message,1)
        d2 = Decision(message,1)
        d3 = Decision(message,2)
        
        row =TableRow()
        row.addDecision(d1)
        row.addDecision(d2)
        row.addDecision(d3)
        self.assertEqual(2,len(row.decisions))
        self.assertEqual(2,row.decisions[0].count)
        self.assertEqual(1,row.decisions[1].count)
