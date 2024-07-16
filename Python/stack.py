class Stack:
    def __init__(self):
        self.s1=[]
    
    def push(self,x):
        self.s1.append(x)
    def pop(self):
        if len(self.s1)==0:
            print("stack is empty")
        else:
            self.s1.pop(-1)

    def isempty(self):
        if len(self.s1)==0:
            return True
        else:
            return False
        

stack= Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.pop()
print(stack.isempty())
