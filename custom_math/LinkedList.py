from __future__ import annotations
from dataclasses import dataclass


@dataclass
class LinkedList:
    head: Node | None = None
    
    def append(self, other: object) -> None:
        if (self.head == None):
            self.head = Node(other)
            return
        
        curr = self.head
        while (curr.next != None):
            curr = curr.next
        
        curr.next = Node(other)
        
    def prepend(self, other: object) -> None:
        new_node = Node(other)
        new_node.next = self.head
        self.head = new_node
        
    def remove(self, val: object) -> bool:
        if (self.head == None or val not in self): return False
        curr = self.head
        if (curr.value == val): self.head = curr.next
        
        while (curr.next != None):
            if (curr.next.value == val):
                curr.next = curr.next.next
                return True
            curr = curr.next
        
        return False
    
    def index(self, val: object) -> int:
        curr = self.head
        i = 0
        while (curr != None):
            if (curr.value == val): return i
            i += 1
            curr = curr.next
        raise ValueError("Value not in LinkedList")
    
    def __len__(self) -> int:
        if (self.head == None): return 0
        
        curr = self.head
        count = 1
        while (curr.next != None):
            count += 1
            curr = curr.next
        
        return count
        
    def __contains__(self, val: object) -> bool:
        if (self.head == None): return False
        
        curr = self.head
        while (curr.next != None):
            if (curr.value == val): return True
            curr = curr.next
        
        return curr.value == val
        
    def __str__(self) -> str:
        if (self.head == None): return ""
        
        s = ""
        curr = self.head
        while (curr.next != None):
            s += str(curr.value) + " "
            curr = curr.next
        s += str(curr.value)
        return s
    
    def __getitem__(self, index: int) -> object:
        if (self.head == None): raise IndexError("LinkedList is empty")
        
        curr = self.head
        i = 0
        while (curr.next != None):
            if (i == index):
                return curr.value
            curr = curr.next
            i += 1
        if (i == index): return curr.value
        raise IndexError(f"Index {index} is out of range for LinkedList of size {len(self)}")
    
    def __setitem__(self, index: int, val: object) -> None:
        if (self.head == None): raise IndexError("LinkedList is empty")
        
        curr = self.head
        i = 0
        while (curr.next != None):
            if (i == index):
                curr.value = val
                return 
            curr = curr.next
            i += 1
        if (i == index): 
            curr.value = val
            return 
        raise IndexError(f"Index {index} is out of range for LinkedList of length {len(self)}")
    
    
@dataclass
class Node:
    value: object
    next: Node | None = None