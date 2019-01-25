class HashTable:
    def __init__(self, size=11, collision_allowed=False):
        self.values = [None] * size
        self.collision_allowed = collision_allowed

    def hash(self, value):
        result = (value + 2) % self.size()
        return result

    def size(self):
        return len(self.values)

    def remove(self, value):
        key = self.hash(value)

        if self.values[key] != value and self.collision_allowed:
            offset = 1
            temp_key = (key + offset) % self.size()

            while self.values[temp_key] is not None:
                offset = +1
                if self.values[temp_key] == value:
                    self.values[temp_key] = None
                    return

        elif self.values[key] == value:
            self.values[key] = None

        else:
            print("Error:This number does not exist")

    def put(self, value):
        key = self.hash(value)
        if self.values[key] is None:
            self.values[key] = value
        elif self.values[key] == value:
            print("Error: Number all ready exists")
            return
        elif self.collision_allowed:
            offset = 1
            temp_key = (key + offset) % self.size()
            while (self.values[temp_key] is not None):
                if self.values[temp_key] == value:
                    print("Error: Number all ready exists")
                    return
                offset += 1
                if offset == self.size():
                    print("HashTable is full. No space.")
                temp_key = (key + offset) % self.size()
            else:
                self.values[temp_key] = value
        else:
            print("There was an error: Hash collision")
            return

    def contains_value(self, value):
        key = self.hash(value)
        if self.collision_allowed == False:
            if self.values[key] != value:
                return False
            return True
        else:
            offset = 0
            while self.values[(key + offset) % self.size()] != value:
                offset += 1
                if offset == self.size() or self.values[(key + offset) % self.size()] is None:
                    return False
            else:
                return True


table = HashTable(11, False)

table.put(10)
table.put(6)
table.put(17)
table.put(18)
table.put(19)

if (table.contains_value(5)):
    print("The value you have eneterd is in the list")
else:
    print("The value you have eneterd is not in the list")

table.remove(11)

print(table.values)

