class StackofStacks:

    def __init__(self, max_height):
        self.stack = [[]]
        self.max_height = max_height
        
    def push(self, data):
        if len(self.stack[-1]) < self.max_height:
           self.stack[-1].append(data)
        else:
            self.stack.append([])
            self.stack[-1].append(data)

    def pop(self):
        if len(self.stack[-1]) > 0:
            self.stack[-1].pop()
        if not self.stack[-1]: # check if bottom stack is now empty
            self.stack.pop()
    def peek(self):
        print(self.stack[-1][-1])
    
    def show(self):
        print(self.stack)

a = StackofStacks(3)

a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.show()
a.pop()
a.peek()
a.show()
a.pop()
a.show()
