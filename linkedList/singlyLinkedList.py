class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.head == None

    def addLast(self, data):
        node = Node(data)

        if self.isEmpty():
            self.head = self.tail = node

        else:
            self.tail.next = node
            self.tail = node

        self.count += 1

    def addFirst(self, data):
        node = Node(data)

        if self.isEmpty():
            self.head = self.tail = node

        else:
            node.next = self.head
            self.head = node    

        self.count += 1

    def indexOf(self, data):
        idx = 0
        curr = self.head

        while curr != None:
            if curr.data == data:
                return idx
            idx += 1
            curr = curr.next

        return -1

    def contains(self, data):
        return self.indexOf(data) != -1

    def removeFirst(self):
        if self.isEmpty():
            return

        elif self.head == self.tail:
            self.head = self.tail = None

        else:
            second = self.head.next
            self.head.next = None
            self.head = second

        self.count -= 1

    def removeLast(self):
        if self.isEmpty():
            return

        elif self.head == self.tail:
            self.head = self.tail = None

        else:
            curr = self.head

            while curr.next != self.tail:
                curr = curr.next

            curr.next = None
            self.tail = curr

        self.count -= 1

    def size(self):
        return self.count

    def toList(self):
        res = []
        curr = self.head
        while curr is not None:
            res.append(curr.data)
            curr = curr.next
        return res

    def reverse(self):
        if self.isEmpty():
            return
        
        elif self.head == self.tail:
            return

        curr = self.head.next
        prev = self.head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.tail = self.head
        self.tail.next = None
        self.head = prev
    
    def getKthfromEnd(self, k: int):
        if k > self.count or k < 1:
            raise Exception("Invalid argument for k.", k)

        a = b = self.head
        for i in range(k - 1):
            b = b.next
        
        while b != self.tail:
            a = a.next
            b = b.next
        
        return a.data

