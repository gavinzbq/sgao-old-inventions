from linlist import Node, LinList
import unittest

class TestNode(unittest.TestCase):

    def test_setdata(self):
        testnode = Node('best sg')
        testnode.set_data('dWade')
        assert testnode.get_data() == 'dWade'

    def test_setnext(self):
        testnode = Node('best sg')
        testnode.set_next('MJ')
        assert testnode.get_next() == 'MJ'


class Testlinlist(unittest.TestCase):

    def setUp(self):
        self.linlist = LinList()
        self.linlist.add('best sg')
        self.linlist.add('dWade')
        self.linlist.add('MJ')

    def test_add(self):
        assert self.linlist.head.get_data() == 'MJ'
        assert self.linlist.head.next.get_data() == 'dWade'

    def test_remove(self):
        self.linlist.remove('dWade')
        assert self.linlist.head.next.get_data() == 'best sg'

    def test_size(self):
        assert self.linlist.size() == 3
