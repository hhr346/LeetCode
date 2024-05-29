'''
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
 

注意：

你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
'''
from collections import deque

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise Exception("Queue is empty")
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0

class MyStack:

    def __init__(self):
        self.stack = Queue()

    def push(self, x: int) -> None:
        self.stack.push(x)

    def pop(self) -> int:
        if not self.empty():
            for count in range(self.stack.size()-1):
                first = self.stack.pop()
                self.stack.push(first)
            outcome = self.stack.pop()
            return outcome
        else:
            raise Exception("Stack is empty")

    def top(self) -> int:
        if not self.empty():
            for count in range(self.stack.size()-1):
                first = self.stack.pop()
                self.stack.push(first)
            outcome = self.stack.pop()
            self.stack.push(outcome)
            return outcome
        else:
            raise Exception("Stack is empty")

    def empty(self) -> bool:
        return self.stack.is_empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == "__main__":
    import sys
    commands = sys.argv[1][1:-1].split(",")
    params = []
    params2 = sys.argv[2][1:-1].split(",")
    for param in params2:
        if param == '[]':
            params.append([])
        else:
            params.append([int(param[1:-1])])
    print(params)

    my_stack = None
    result = []

    for command, param in zip(commands, params):
        print(command)
        if command == "MyStack":
            my_stack = MyStack()
            result.append(None)
        elif command == "push":
            my_stack.push(*param)
            result.append(None)
        elif command == "pop":
            result.append(my_stack.pop())
        elif command == "top":
            result.append(my_stack.top())
        elif command == "empty":
            result.append(my_stack.empty())

    print(result)
