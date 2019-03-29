# Author: O98K
"""
    Stack()     创建一个空的新栈，它不需要参数，并返回一个空栈
    push(item)  将一个新项添加到栈的顶部。它需要item做参数并不返回任何内容
    pop()       从栈中删除顶部项。它不需要参数并返回item，栈被修改
    peek()      从栈返回顶部项，但不会删除它。不需要参数，不修改栈
    isEmpty()   测试栈是否为空。不需要参数，并返回布尔值
    size()      返回栈中的 item 数量。不需要参数，并返回一个整数
"""


class Stack(object):
    """
        模拟 栈
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 栈操作
# stack = Stack()
# print('stack is empty ===>', stack.isEmpty())
# stack.push('name')
# print(stack.size())
# print(stack.peek())
# stack.push('age')
# print(stack.pop())


# def parchecker(symbolstring, stack):
#     """
#         括号匹配
#     """
#     balance = True
#     index = 0
#     while index < len(symbolstring) and balance:
#         symbol = symbolstring[index]
#         if symbol == "(":
#             stack.push(symbol)
#         else:
#             if stack.isEmpty():
#                 balance = False
#             else:
#                 stack.pop()
#
#         index += 1
#     if balance and stack.isEmpty():
#         return True
#     else:
#         return False


def parchecker(symbolstring, stack):
    """
        括号匹配
    """
    balance = True
    index = 0
    while index < len(symbolstring) and balance:
        symbol = symbolstring[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balance = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balance = False
        index += 1
    if balance and stack.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


stack = Stack()
# symbolstring = '(((())))'
symbolstring = '{{([][])}()}'
print(parchecker(symbolstring, stack))
