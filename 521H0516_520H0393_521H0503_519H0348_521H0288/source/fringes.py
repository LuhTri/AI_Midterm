class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        self.items.insert(0, (priority, item))
        self.items.sort()

    def dequeue(self):
        return self.items.pop(0)[1]

    def is_empty(self):
        return len(self.items) == 0
