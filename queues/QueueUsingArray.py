class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is already empty!.")
        return self.queue.pop(0)


    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is already empty!.")
        return self.queue[0]
