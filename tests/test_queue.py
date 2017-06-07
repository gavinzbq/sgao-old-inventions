from queue import Queue
import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue('MJ')
        self.queue.enqueue(23)
        self.queue.enqueue('dWade')
        self.queue.enqueue(3)

    def test_enqueue(self):
        assert len(self.queue.items) == 4

    def test_dequeue(self):
        assert self.queue.dequeue() == 'MJ'
        assert len(self.queue.items) == 3

    def test_front(self):
        assert self.queue.front() == 'MJ'
        assert len(self.queue.items) == 4 

    def test_end(self):
        assert self.queue.end() == 3
        assert len(self.queue.items) == 4 

    def test_size(self):
        assert len(self.queue.items) == self.queue.size()
