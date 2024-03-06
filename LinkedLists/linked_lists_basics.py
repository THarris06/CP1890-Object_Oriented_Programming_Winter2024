from dataclasses import dataclass


@dataclass
class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"Node: {self.data}"


test1 = Node(2)
print(test1)


@dataclass
class LinkedList:

    def __init__(self):
        self.head = None
        self.nodes = []

    def __repr__(self):
        self.nodes = []
        node = self.head
        while node is not None:
            self.nodes.append(str(node.data))
            node = node.next_node
        self.nodes.append('None')
        return '->'.join(self.nodes)

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_in_middle(self, data, position):
        new_node = Node(data)
        pos = 0
        current_node = self.head
        if pos == position:
            self.insert_at_head(new_node)

        else:
            while current_node is not None and (pos + 1) != position:
                pos = pos + 1
                current_node = current_node.next_node

            if current_node is not None:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
            else:
                print('position does not exist.')

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = new_node

    def delete_at_head(self):
        self.head = self.head.next_node

    def delete_at_tail(self):
        if self.head is None:
            print(' linked list is empty.')

            
llist = LinkedList()
# print(llist)

first_node = Node('a')
llist.head = first_node
second_node = Node('b')
third_node = Node('c')

first_node.next_node = second_node
second_node.next_node = third_node

llist.insert_at_head(0)
print(llist)
llist.insert_at_tail(100)
print(llist)
llist.insert_in_middle(20, 2)

print(llist)
llist.delete_at_head()
print(llist)
