'''
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：

你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
'''

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")
    
    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0
    

class MyQueue:

    def __init__(self):
        self.queue = Stack()
        self.assist = Stack()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        if not self.queue.is_empty():
            # Pipe out the elements in the QUEUE to the ASSIST
            while not self.queue.is_empty():
                popcorn = self.queue.pop()
                self.assist.push(popcorn)
            outcome = self.assist.pop()

            # Pipe out the elements in the ASSIST back to QUEUE
            while not self.assist.is_empty():
                popcorn = self.assist.pop()
                self.queue.push(popcorn)
        else:
            raise Exception("Queue is self.empty")
        return outcome


    def peek(self) -> int:
        if not self.queue.is_empty():
            # Pipe out the elements in the QUEUE to the ASSIST
            while not self.queue.is_empty():
                popcorn = self.queue.pop()
                self.assist.push(popcorn)
            outcome = self.assist.pop()
            self.queue.push(outcome)

            # Pipe out the elements in the ASSIST back to QUEUE
            while not self.assist.is_empty():
                popcorn = self.assist.pop()
                self.queue.push(popcorn)
        else:
            raise Exception("Queue is empty")
        return outcome

    def empty(self) -> bool:
        return self.queue.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
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

    my_queue = None
    result = []

    for command, param in zip(commands, params):
        print(command)
        if command == "MyQueue":
            my_queue = MyQueue()
            result.append(None)
        elif command == "push":
            my_queue.push(*param)
            result.append(None)
        elif command == "pop":
            result.append(my_queue.pop())
        elif command == "peek":
            result.append(my_queue.peek())
        elif command == "empty":
            result.append(my_queue.empty())

    print(result)
