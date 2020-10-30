class Stack:
    #创建空栈 
    def __init__(self):
        self.items = []
    #判断空表
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def traverse(self):
        print(self.items)

if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print(stack.size())
    stack.traverse()
    print(stack.peek())
    stack.pop()
    stack.traverse()