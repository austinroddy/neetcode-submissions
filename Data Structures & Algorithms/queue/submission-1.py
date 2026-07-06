class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left


    def isEmpty(self) -> bool:
        if self.left.next == self.right:
            return True
        else:
            return False


    def append(self, value: int) -> None:
        old_last = self.right.prev # save off the right hand prev
        new_node = Node(value) # new node
        new_node.prev = old_last # new nodes previous is rights old previous
        new_node.next = self.right # new nodes next is the right sentinal
        self.right.prev = new_node # finally make the old rights previous tied to new node
        old_last.next = new_node # make the right previous's next tied to the new node
        

    def appendleft(self, value: int) -> None:
        old_next = self.left.next # save off the old next
        new_node = Node(value) # make new node
        new_node.next = old_next # [left]<->[new]<->[old node]
        new_node.prev = self.left
        self.left.next = new_node
        old_next.prev = new_node


    def pop(self) -> int:
        if not self.isEmpty():
            node_to_remove = self.right.prev # save off node to delete
            self.right.prev = node_to_remove.prev # set right prev to the skip the node to delete a
            node_to_remove.prev.next = self.right # set node to remove's prev to self.right
            return node_to_remove.val
        else:
            return -1


    def popleft(self) -> int:
        if not self.isEmpty():
            node_to_remove = self.left.next 
            self.left.next = node_to_remove.next 
            node_to_remove.next.prev = self.left 
            return node_to_remove.val
        else:
            return -1
        
