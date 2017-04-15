# Shanyun Gao
# linked list data structure

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext

class LinList:

    def __init__(self):
        self.head = None

    def add(self,item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def remove(self,item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
        else:
            print ('The item is not in the list.')

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self,item):
        current = self.head
        found = False

        while not found and current != None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def is_empty(self):
        return self.head == None
