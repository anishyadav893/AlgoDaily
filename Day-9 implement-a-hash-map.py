# This is my solution for AlgoDaily problem Implement a Hash Map
# Located at https://algodaily.com/challenges/implement-a-hash-map

class Node:
  def __init__(self, key, value):
    self.key = key
    self. value = value
    
class Hashmap:
    def __init__(self):
      self.storage = [None for _ in range(16)]
      self.size = 0
      
    def hashStr(self, key):
      if isinstance(key, int):
        return key
      
      result = 5381
      for char in key:
        result = 33 * result + ord(char)  
      return result
    
    def position(self, key_hash_value):
      return key_hash_value % 16
    
    def set(self, key, val):
      p = Node(key, val)
      key_hash_value = self.hashStr(key)
      index = self.position(key_hash_value)
      
      if not self.storage[index]:
        self.storage[index] = [p]
        self.size += 1
      else:
        list_at_idx = self.storage[index]
        if p not in list_at_idx:
          self.storage[index] = [p]
          self.size += 1
        else:
          for i in self.storage[index]:
            if i == p:
              i.value = val
              break
      
    
    def get(self, key):
      key_hash_value = self.hashStr(key)
      index = self.position(key_hash_value)
      
      if not self.storage[index]:
        return None
      else:
        list_at_idx = self.storage[index]
        for i in self.storage[index]:
            if i.key == key:
              return i.value
      return None

