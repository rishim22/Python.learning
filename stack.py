class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack)==0:
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack)==0:
            return "Stack is empty"
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:", s.stack)
print("Peek:", s.peek())
print("Pop:", s.pop())
print("After Pop:", s.stack)
            
    
