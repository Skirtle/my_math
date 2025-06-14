from typing import Self

class Node:
    def __init__(self, value = None):
        self.next = None
        self.value = value
        
    def __str__(self) -> str: return f"Node({self.value})"
    def __repr__(self) -> str: return self.__str__()
    

class SinglyLinkedList:
    head: Node = None
    
    def __init__(self, *nodes: Self):
        if (len(nodes)) > 0:
            self.head = nodes[0]
            
            curr_node = self.head
            for node in nodes:
                if (node == self.head): continue
                curr_node.next = node
                curr_node = node
                
    def append(self, new_node) -> None:
        self[-1].next = new_node
                
    def __iter__(self):
        self._iter_node = self.head
        return self
    
    def __next__(self):
        node = self._iter_node
        if (node == None): raise StopIteration
        self._iter_node = self._iter_node.next
        return node
                
    def __str__(self) -> str: return str([x for x in self])
    def __repr__(self) -> str: return self.__str__()
    def __getitem__(self, index): return [x for x in self][index]
    def __setitem__(self, index, new_item) -> None:
        if (index >= len(self)): raise IndexError(f"{type(self).__name__} assignment out of range")
        if (not isinstance(new_item, Node)): raise TypeError(f"expected type '{Node.__name__}', got type '{type(new_item).__name__}' instead")
        
        print(f"Replacing index at {index} with {new_item}")
        
        if (index == 0):
            new_item.next = self.head.next
            self.head = new_item
        elif (index == 1):
            temp = self.head.next
            self.head.next = new_item
            new_item.next = temp
        elif (index == len(self) - 1):
            self[index - 1].next = new_item
        else:
            for i,v in enumerate(self):
                if (i == index): # Found the index
                    temp = self[i + 1]
                    self[i - 1].next = new_item
                    self[i].next = temp
        
            
        
        
    def __len__(self) -> int: return len([x for x in self])
        
                

if __name__=="__main__":
    print(f"Testing LinkedList.py")
    sing_list = SinglyLinkedList(Node(10), Node(9), Node(8), Node(7))
    
    for i in range(len(sing_list)):
        new_node = Node(sing_list[i].value * 2)
        new_node.next = sing_list[i].next
        sing_list[i] = new_node
    
    sing_list.append(Node(12))
    print(sing_list)
    