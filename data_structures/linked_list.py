class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def __str__(self):
        current = self.head
        strings = []
        while current is not None:
            strings.append(str(current.value))
            current = current.next
        return ' -> '.join(strings)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(6)
    ll.add(10)
    ll.add(1)
    print(ll)  # 1 -> 10 -> 6

