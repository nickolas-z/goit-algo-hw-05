class HashTable:
    def __init__(self, size)->None:
        """ Constructor of the HashTable class """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key)->int:
        """ Hash function """
        return hash(key) % self.size

    def insert(self, key, value)->bool:
        """ Inserting a new key-value pair into the HashTable """
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key)->int:
        """ Getting a value by key """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key)->bool:
        """ Deleting a key-value pair by key """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is None:
            return False
        for i in range(len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True
        return False
    
    def keys(self)->list:
        """ Getting all keys from the HashTable """
        keys = []
        for i in self.table:
            if i:
                for j in i:
                    keys.append(j[0])
        return keys

    def __str__(self)->str:
        """ String representation of the HashTable """
        items = []
        for item in self.table:
            for key, value in item:
                items.append(f"{key}: {value}")
        return "{" + ", ".join(items) + "}"

if __name__ == "__main__":
    # test the HashTable class
    H = HashTable(5)
    
    # Inserting key-value pairs
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)
    H.insert("grape", 40)
    H.insert("pineapple", 50)
    
    # Display the HashTable
    print(f"\nHashTable: {H}")
    
    # remove a key-value pair
    H.delete("apple")
    print(f'H.delete("apple")')
    
    # Display the HashTable after removing a key-value pair
    print(f"HashTable after remove: {H}\n")
