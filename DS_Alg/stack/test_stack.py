from stack import Stack
import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push('MJ')

    def test_push(self):
        self.stack.push('dWade')
        assert len(self.stack.items) == 4

    def test_pop(self):
        assert self.stack.pop() == 'MJ'
        assert len(self.stack.items) == 2 

    def test_size(self):
        assert self.stack.size() == len(self.stack.items)

    def test_peek(self):
        assert self.stack.peek() == 'MJ'
        assert len(self.stack.items) == 3 
