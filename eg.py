lass Node:
 def __init__(self,dataa):
  self.data=dataa
  self.next=None
class Linkedlist:
      def __init__(self):
          self.head=None
class Printlist:
     def print(self):
        self.printval=printdata
      while printdata is not None:
       print(printdata.data)
       printdata=printdata.next
              
      def insertAtbeg(newdata):
          newnode=Node(newdata)
          newnode.next=self.head
          self.head=newnode
          
llob=Linkedlist()
llob.head=Node("mon")
llob1=Node("tue")
llob2=Node("wed")

llob.head.next=llob1
llob1.next=llob2
llob2.next=None

Linkedlist.insertAtbeg("sun")
print(linkedlist.insertAtbeginning())
temp=llob.head
while temp:
    print(temp.data," ==> ",'')
    temp=temp.next
