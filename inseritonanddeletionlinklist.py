class Node:
 def __init__(self,data):
  self.data=data
  self.next=None
 
class LinkedList:
 def __init__(self):
  self.head=None
   
 def insert(self,data):
  if(self.head==None):
   self.head=Node(data)
  else:
   current=self.head
   while(current.next!=None):
    current=current.next
   current.next=Node(data)
 
 def insert_at_beg(self,data):
  newnode=Node(data)
  newnode.next=self.head
  self.head=newnode
 
 def delete_at_beg(self):
  current=self.head
  self.head=current.next
  del current
 
 def printlist(self):
  current=self.head
  while(current!=None):
   print(current.data)
   current=current.next
 
myLinkList=LinkedList()
myLinkList.insert(25)
myLinkList.insert(45)
myLinkList.insert(78)
print("\n\nCreated Linked List is: \n")
myLinkList.printlist()
print("\n\nEnter the element you want to insert at the beginning: ")
element=int(input())
myLinkList.insert_at_beg(element)
print("\n\nThe updated Linked List after insertion at beginning: \n")
myLinkList.printlist()
print("\n\nThe updated Linked List after deletion at beginning:\n")
myLinkList.delete_at_beg()
myLinkList.printlist()