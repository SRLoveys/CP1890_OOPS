from dataclasses import dataclass


@dataclass
class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __repr__(self):
        return f'Node: {self.data}'


test1 = Node(2)
print(test1)


@dataclass
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.nextNode
        nodes.append("None")
        return "->".join(nodes)

    def insert_at_head(self, data):
        new_node_beg = Node(data)
        if self.head is None:
            self.head = new_node_beg
            return
        else:
            new_node_beg.nextNode = self.head
            self.head = new_node_beg

    def insert_at_end(self, data):
        new_node_end = Node(data)
        if self.head is None:
            self.head = new_node_end
            return

        current_node = self.head
        while current_node.nextNode:
            current_node = current_node.nextNode

        current_node.nextNode = new_node_end

    def insert_at_pos(self, data, position):
        new_node_pos = Node(data)
        current_node = self.head
        pos = 0

        if pos == position:
            self.insert_at_end(new_node_pos)
        else:
            while current_node is not None and (pos+1) != position:
                pos = pos + 1
                current_node = current_node.nextNode

            if current_node is not None:
                new_node_pos.nextNode = current_node.nextNode
                current_node.nextNode = new_node_pos
            else:
                print("Position does not exist")


llist = LinkedList()
# print(llist)

firstNode = Node('a')
llist.head = firstNode

secondNode = Node('b')
thirdNode = Node('c')

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

llist.insert_at_head(0)
llist.insert_at_end(100)
llist.insert_at_pos(50, 2)

print(llist)
