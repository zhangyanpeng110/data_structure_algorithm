# Author: O98K


"""
    队列实现

    Queue()         创建一个空的新队列，它不需要参数，并返回一个空队列
    enqueue(item)   将新项添加到队尾，它需要item作为参数，并不返回任何内容
    dequeue()       从队首移除项，它不需要参数并返回item，队列被修改
    isEmpty()       查看队列是否为空，它不需要参数，并返回布尔值
    size()          返回队列中的项数，它不需要参数，并返回一个整
"""


class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue('name')
queue.enqueue('age')
print(queue.size())
print(queue.dequeue())


