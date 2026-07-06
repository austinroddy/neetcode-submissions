class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1  # out of bounds

        # walk to the index
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.val


    def insertHead(self, val: int) -> None:
        new_node = Node(val) # Make a new head node
        new_node.next = self.head # Save off the old head as the 'next' head
        self.head = new_node # update current head with newest node
        self.length += 1 # update the len of the linked list
        if self.tail is None:
            self.tail = self.head


    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.insertHead(val) # if the list is empty, just use insertHead, theres no difference
        else:
            new_node = Node(val) # make a new tail node
            new_node.next = None # set the next node to none as theres nothing after this
            self.tail.next = new_node # set the old tails next to the new tail node
            self.tail = new_node # finally update the old tail to the new tail
            self.length += 1 # update the len of the linked list


    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False  # out of bounds

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None  # list is now empty, tail must reset too
            return True

        # walk to the predecessor (index - 1)
        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next

        # current_node is now at position (index - 1)
        node_to_remove = current_node.next
        current_node.next = node_to_remove.next

        if node_to_remove == self.tail:
            self.tail = current_node  # we removed the tail, update it

        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        # output each value into an array:
        current_node = self.head
        array = []
        for _ in range(self.length):
            array.append(current_node.val)
            current_node = current_node.next
        return array
        
