from Linkedlist.Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)

        # Checking to see if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        # Set the next_element of the previous node to new node
        temp.next_element = new_node
        new_node.previous_element = temp
        return

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        if self.is_empty():
            self.head_node = temp_node
            return self.head_node

        temp_node.next_element = self.head_node
        self.head_node.previous_element = temp_node
        self.head_node = temp_node
        return self.head_node

    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while temp.next_element is not None:
            if temp.data == dt:
                return temp
            temp = temp.next_element

        print(dt, " is not in List!")
        return None

    def delete_at_head(self):
        # Get Head and firstElement of List
        head = self.head_node
        first_element = head.next_element
        # If List is not empty then link head to the
        # next_element of firstElement.
        if first_element is not None:
            head.next_element = first_element.next_element

    def delete(self, dt):
        deleted = False
        if self.is_empty():
            print("List is Empty")
            return deleted
        if self.head_node.next_element.data == dt:
            self.delete_at_head()
            deleted = True

        temp_node = self.head_node.next_element
        previous_node = None

        # Traversing/Searching for Node to Delete
        while temp_node is not None:
            if dt == temp_node.data:
                previous_node.next_element = temp_node.next_element
                deleted = True
                break
            previous_node = temp_node
            temp_node = temp_node.next_element

        if not deleted:
            print(dt, " is not in List!")
        else:
            print(dt, " is deleted!")
        return deleted

    def remove_duplicates(self):
        current_node = self.get_head()
        prev_node = self.get_head()
        # To store values of nodes which we already visited
        visited_nodes = set()
        # If List is not empty and there is more than 1 element in List
        if not self.is_empty() and current_node.next_element is not None:
            while current_node is not None:
                value = current_node.data
                if value in visited_nodes:
                    # current_node is a duplicate as its value is already in the HashSet
                    # so connect prev_node with current_node's next element to remove it
                    prev_node.next_element = current_node.next_element
                    current_node = current_node.next_element
                    continue
                visited_nodes.add(current_node.data)  # Visiting current_node for first time
                prev_node = current_node
                current_node = current_node.next_element

        return self

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def length(self):
        # start from the first element
        curr = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length


# Helper Function to convert List elements in a single string
def elements(lst):
    elementsList = ""
    if lst is None:
        return elementsList

    start = lst.get_head()

    while (start != None):
        elementsList += str(start.data)
        elementsList += "->"
        start = start.next_element
    elementsList += "None"
    return elementsList


def insert_loop(lst):
    temp = lst.get_head()
    while temp.next_element is not None:
        temp = temp.next_element
    temp.next_element = lst.get_head()
