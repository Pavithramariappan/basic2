class stack:                       
    def __init__(self):
        self.stack=[]

    def add(self,dataval):
       #if dataval not in self.stack:
          self.stack.append(dataval)
          #return True
       #else:
          #return False
    def peek(self):
       return self.stack[-1]
    
    def remove(self):
       if len(self.stack)<=0:
          return "no element in the stack"
       else:
          return self.stack.pop()
    def printi(self):
       print(self.stack)
s=stack()
s.add(4)
s.add('pavi')
s.printi()
print(s.peek())
s.remove()
s.printi()
