#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        if init_size:
            self.size = init_size
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        best case and average case is O(n) because you need to loop over each bucket and each linked list within the bucket, this n is the total
        number of key value pairs
        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        best case and average case is O(n) because you need to loop over each bucket and each linked list within the bucket, this n is the total
        number of key value pairs
        """
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

            

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        best case and average case is O(n) because you need to loop over each bucket and each linked list within the bucket, this n is the total
        number of key value pairs
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?
        it will always be O(1) because there is no looping
        """
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        # length = 0
        # for bucket in self.buckets:
        #     length += bucket.length()
        # return length
        return self.size


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?
        average running time is O(l) it takes the average length of each bucket 
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        # def check_key(bucket, key):
            

        # bucket = self.buckets[self._bucket_index(key)]
        bucket = self.get_bucket(key)

        for bucket_key, value in bucket.items():
            if bucket_key  == key:
                return True
        return False
        
        # if bucket.find(lambda item: item == key):
        #     return True
        # else:
        #     return False
        # lambda item: item == key


       


        




    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        average running time is O(l), it takes the average length of each bucket
        """
        # TODO: Find bucket where given key belongs
        # bucket = self.buckets[self._bucket_index(key)]
        bucket = self.get_bucket(key)
        # TODO: Check if key-value entry exists in bucket
        if self.contains(key):
            # return bucket.find(lambda item: item == key)[1]
            for bucket_key, value in bucket.items():
                if bucket_key == key:
                    return value
        else:
            raise KeyError('Key not found: {}'.format(key))
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))





    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?
        average running time is O(l), it takes the average length of each bucket's linked list 
        """
        # TODO: Find bucket where given key belongs
        bucket = self.get_bucket(key)
        tmp_tuple = (key, value)
        
        
        if self.contains(key):
            bucket.replace((key, self.get(key)), (key, value))
        else:
            bucket.append(tmp_tuple)
            self.size += 1
    




        # tmp_tuple = (key, value)
        # if bucket.find(lambda item: item == key) == key:
        #     bucket.replace((key, value), (key, value+1))
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        average running time is O(l) because it will take the average length of each linked list to find the 
        right thing to delete
        """
        
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        bucket = self.get_bucket(key)
        tmp_tuple = (key, self.get(key))
        if self.contains(key):
            bucket.delete(tmp_tuple)
            self.size -= 1
         
        else:
            raise KeyError('Key not found: {}'.format(key))
            



    def get_bucket(self, key):
        return self.buckets[self._bucket_index(key)]


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
