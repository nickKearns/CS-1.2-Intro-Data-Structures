#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None #self.next is always a different Node object

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.num_nodes = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?
        O(n) because there is a while loop where you are forced to iterate over the entire list of nodes
        
        """
        #TODO: Loop through all nodes and count one for each
        # length = 1
        if self.is_empty():
            return 0
        # current_node = self.head
        # while current_node.next is not None:
        #     length += 1
        #     current_node = current_node.next
        # return length
        return self.num_nodes
        # return len(self.items()) this works too
        



    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        O(1) constant time. There are no loops to increase the time complexity 
        """
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        self.num_nodes += 1
        tmp_node = Node(item)
        is_tmp_node_new_tail = False


        if self.head is None:
            self.head = tmp_node
            if self.tail is None:
                self.tail = tmp_node
                is_tmp_node_new_tail = True

        if not is_tmp_node_new_tail:
            self.tail.next = tmp_node
            self.tail = tmp_node
        



    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        O(1) constant time, no loops
        """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        tmp_node = Node(item)
        is_tmp_node_new_head = False
        self.num_nodes += 1

        if self.head is None:
            self.head = tmp_node
            is_tmp_node_new_head = True
            if self.tail is None:
                self.tail = tmp_node
        if not is_tmp_node_new_head:
            tmp_node.next = self.head
            self.head = tmp_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?
        O(1) is the best case because what you want to find could be the head node
        O(n) is the worst case because you would be looping through n items
        """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        #quality is a function?
        node = self.head
        while node is not None:
            if quality(node.data) == True:
                return  node.data
            node = node.next
        return None

        
    def replace(self, item_to_delete, new_item):
        node = self.head
        while node is not None:
            if node.data == item_to_delete:
                node.data = new_item
                break
            node = node.next




    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?
        O(1) is best case because what you want to delete could be the first node
        O(n) is worst case because you might have to iterate over the entire linked list 

        """
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        
        print(self.length())
        if self.length() == 0:
            raise ValueError('Item not found: {}'.format(item))

        node = self.head
        next_node = self.head.next
        found_item = False

        if self.head.data == item:
            self.head = self.head.next
            found_item = True
            if self.length() == 0:
                self.tail = None
        while next_node is not None:
            
            if next_node.data == item:
                node.next = next_node.next
                found_item = True
                if next_node == self.tail:
                    self.tail = node
                    break
                break

                
            node = next_node
            next_node = next_node.next

            print("head: {}".format(self.head))
            print("tail: {}".format(self.tail))
        if found_item:
            self.num_nodes -= 1
        else:
            raise ValueError('Item not found: {}'.format(item))

            





def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))
    print('replace A with B {}'.format(ll))
    ll.replace('A', 'B')
    print(ll)

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['A', 'B', 'C']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))




if __name__ == '__main__':
    test_linked_list()
