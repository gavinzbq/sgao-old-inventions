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
        assert self.stack.peek() == 'dWade'

    def test_pop(self):
        assert self.stack.pop() == 'MJ'
        assert self.stack.peek() == 5

    def test_size(self):
        assert self.stack.size() == 3

    def test_peek(self):
        assert self.stack.peek() == 'MJ'
