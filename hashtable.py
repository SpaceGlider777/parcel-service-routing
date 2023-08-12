class HashTable:
    '''
    The data structure to hold package data.
    '''

    def __init__(self, size):
        '''
        Constructor which takes an integer size to set the number of buckets.
        '''
        self.size = size
        self.table = []
        for _ in range(size):
            self.table.append([])

    def __str__(self):
        '''
        Returns a string which displays all packages in order.
        '''
        items = []
        for bucket in self.table:
            for item in bucket:
                items.append(item)
        items.sort(key=lambda i: i.id)

        table_str = ''
        for item in items:
            table_str += item.__str__() + '\n'
        return table_str

    def insert(self, key, value):
        '''
        Space: O(1)
        Time: O(1)
        Inserts a value into the hash table given a key.
        '''
        hash_key = hash(key) % self.size
        self.table[hash_key].append(value)

    def remove(self, key):
        '''
        Space: O(1)
        Time: average O(1), worse case O(n)
        Removes a value into the hash table given a key.
        '''
        hash_key = hash(key) % self.size
        for item in self.table[hash_key]:
            if key == item.id:
                self.table[hash_key].remove(item)

    def get(self, key):
        '''
        Space: O(1)
        Time: average O(1), worse case O(n)
        Returns a value into the hash table given a key.
        '''
        hash_key = hash(key) % self.size
        for item in self.table[hash_key]:
            if key == item.id:
                return item
        return None
    