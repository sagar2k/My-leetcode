#chaining implementation of hashset
#have a dummy node (-1,-1) at each array index-


class node:
    def __init__(self,value):
        self.value=value
        self.next=None


class MyHashSet:

    def __init__(self):
        self.array=[-1 for i in range(10000)]
    
    def find(self,head,key):
        prev=None
        current=head
        while current!=None and current.value!=key:
            prev=current
            current=current.next
        return prev
            
        

    def add(self, key: int) -> None:
        hash_key=key%10000
        if self.array[hash_key]==-1:
            self.array[hash_key]=node(-1)
        
        
            #if that key is already in linked list then ignore,if not add to end of linked list 
        prev=self.find(self.array[hash_key],key)
           
        if prev.next==None:#prev is last element
                prev.next=node(key)
        
        return
            
        
    
        

    def remove(self, key: int) -> None:
        hash_key=key%10000
        if self.array[hash_key]==-1:
            return
        else:
            prev=self.find(self.array[hash_key],key)
            
            
            #key not found
            if prev.next==None:
                return
            #key found
            else:
                prev.next=prev.next.next
        return
            
        

    def contains(self, key: int) -> bool:
        #print(self.array)
        hash_key=key%10000
        if self.array[hash_key]==-1:
            return False
        else:
            prev=self.find(self.array[hash_key],key)
            
            if prev.next==None:
                return False
            else:
                return True
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
