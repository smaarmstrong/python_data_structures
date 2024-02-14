class Node:
    # constructor
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    # constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)

        # if the linked list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        # else append to the tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        # why is this returning True?
        # apparently there is no clear reason and it seems to be an idiosyncracy of the teacher!
        return True


my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.print_list()


