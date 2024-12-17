class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

# O(1) - constant time
    def __len__(self):
        return self.size

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError("Key not found")

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError("Key not found")

    # O(n) - linear time
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    # O(n) - linear time
    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    # O(n) - linear time
    def items(self):
        return [(k,v) for bucket in self.buckets for k, v in bucket]

    # O(k) - linear in key length
    def _hash_function(self, key):
        keyString = str(key)
        hashResult = 0

        for c in keyString:
            hashResult = (hashResult * 31 + ord(c)) % self.capacity
        return hashResult


def main():
    hashMap = HashMap(32)

    hashMap.put("name", "Mike")
    hashMap.put("age", 30)
    hashMap.put("job", "Programmer")

    print(hashMap.items())

    print(hashMap.buckets)

###############################################
# for testing how good our hash funciton is
    import matplotlib.pyplot as plt
    import uuid

    hashMap = HashMap(100)

    for _ in range(1000):
        hashMap.put(uuid.uuid4(), "someValuee")
    
    X = []
    y = []
    
    for i, bucket in enumerate(hashMap.buckets):
        X.append(i)
        y.append(len(bucket))
    
    plt.bar(X,y)
    plt.show()

################################################

if __name__ == "__main__":
    main()