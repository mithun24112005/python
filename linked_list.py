# linked lists
class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class linked_list:
    def __init__(self):
        #empty linked list--> 0 nodes
        self.head=None
        self.n=0 #count--->no of nodes
    def __len__(self): #length-->no of nodes in the ll
        return self.n
    def insert_head(self,value):
        new_node=node(value)
        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1
    
    def __str__(self):
        curr=self.head
        result=''
        while curr!=None:
            # print(curr.data)
            result=result+str(curr.data)+'->'
            curr=curr.next
        return result[:-2]
    
    def append(self,value):
        new_node=node(value)
        if self.head==None:
            # empty
            self.head=new_node
            self.n+=1
            return
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        self.n+=1
    
    def insert_after(self,after,value): #after --> kis node ke bad dalna he
        new_node=node(value)
        curr=self.head
        while curr!=None:
            if curr.data==after:
                break
            curr=curr.next
        if curr!=None:
            new_node.next=curr.next
            curr.next=new_node
            print(curr.data)
            self.n+=1
        else:
            return "item not found"
    
    def clear(self):
        self.head=None
        self.n=0
    def delete_head(self):
        if self.head==None:
            return 'empty LL'
        self.head=self.head.next
        self.n-=1
    
    def pop(self):
        if self.head==None:
            return 'empty ll'
        curr=self.head
        if curr.next==None:
            self.delete_head()
            return
        while curr.next.next!=None:
            curr=curr.next
        curr.next=None
        self.n-=1
    
    def remove(self,value):
        if self.head==None:
            return 'empty LL'
        if self.head.data==value:
            return self.delete_head()
        curr=self.head
        while curr.next!=None:
            if curr.next.data==value:
                break
            curr=curr.next
        if curr.next==None:
            return "not found"
        else:
            curr.next=curr.next.next
    
    def search(self,item):
        curr=self.head
        pos=0
        while curr!=None:
            if curr.data==item:
                return pos
            curr=curr.next
            pos=pos+1
        return 'not found'
    
    def __getitem__(self,index):
        curr=self.head
        pos=0
        while curr!=None:
            if pos==index:
                return curr.data
            curr=curr.next
            pos+=1
        return 'index error'
    
    def replace_max(self,value):
        temp=self.head
        max=temp.data
        while temp!=None:
            if temp.data>max:
                max=temp
            temp=temp.next
        max.data=value

    def add_odd(self):
        temp=self.head
        counter=0
        while temp!=None:
            if counter%2!=0:
                result=result+temp.data
            counter+=1
            temp=temp.next
        print(result)
    
    

l=linked_list()
l.insert_head(1)
l.insert_head(2)
l.append(5)
l.insert_head(3)
l.add_odd()
# l.pop()
# l.delete_head()
# l.clear()
# print(l.remove(4))
# l.pop()
# print(l.insert_after(5,200))
# l.insert_after(2,200)
# print(l.insert_after(4,200))
print(l.search(3))
l.replace_max(17)
print(l[1])
print(len(l))
print(l)

# a=node(1)
# b=node(2)
# c=node(3)
# a.next=b
# b.next=c
# print(a.data,a.next)
# print(b.data,b.next)
# print(c.data,c.next)
# print(id(a))