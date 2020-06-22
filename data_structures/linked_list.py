class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def delete(self, value):
        if self.head is None:
            raise ValueError(f'value {value} is not in the list')
        if self.head.value == value:
            self.head = self.head.next
        else:
            prev = self.head
            current = self.head.next
            while current.value != value:
                if current.next is None:
                    raise ValueError(f'value {value} is not in the list')
                current = current.next
                prev = prev.next
            prev.next = current.next

    def __contains__(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        current = self.head
        strings = []
        while current is not None:
            strings.append(str(current.value))
            current = current.next
        return ' -> '.join(strings)

    def __iter__(self):
        # 6 -> 1 -> 12
        current = self.head
        while current is not None:
            yield current.value
            current = current.next


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(6)
    ll.add(1)
    ll.add(3)
    ll.add(8)
    for item in ll:
        print(item)

    # print(ll)  # 1 -> 10 -> 6

