class List:
    class ListItem:
        def __init__(self, value, prev, next):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        if self.tail is None:
            self.head = self.tail = self.ListItem(value, None, None)
        else:
            new_item = self.ListItem(value, self.tail, None)
            self.tail.next = new_item
            self.tail = new_item

    def pop(self):
        if self.tail is not None:
            if self.tail.prev is not None:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = None
                self.head = None

    def shift(self):
        if self.head is not None:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None

    def unshift(self, value):
        if self.head is None:
            self.head = self.tail = self.ListItem(value, None, None)
        else:
            new_item = self.ListItem(value, None, self.head)
            self.head.prev = new_item
            self.head = new_item

    def print(self):
        item = self.head
        contents_str = ""
        while item is not None:
            contents_str += f"{item.value} "
            item = item.next
        contents_str = "[" + contents_str + "]"
        print(contents_str)


list_sample = List()
print("Empty list:")
list_sample.print()

list_sample.push(1)
list_sample.push(2)
list_sample.push(3)
print("Added elements 1, 2, 3. Expected contents: 1 2 3")
list_sample.print()

list_sample.pop()
print("Removed last element. Expected contents: 1 2")
list_sample.print()

list_sample.push(4)
list_sample.push(5)
print("Added elements 4, 5 to the end. Expected contents: 1 2 4 5")
list_sample.print()

list_sample.shift()
print("Removed first element. Expected contents: 2 4 5")
list_sample.print()

list_sample.unshift(7)
print("Added element 7 to the beginning. Expected contents: 7 2 4 5")
list_sample.print()
