import hashlib
import json
import datetime;

class Block:

  def __init__(self, index, data_dict, previous_hash = ''):
    self.index = index
    self.data_dict = data_dict
    self.previous_hash = previous_hash
    self.timestamp = self.get_timestamp()
    self.hash = self.generate_hash()

  def generate_hash(self):
    hash_string = str(self.index) + self.timestamp + str(json.dumps(self.data_dict)) + self.previous_hash
    return hashlib.sha256(hash_string.encode()).hexdigest()

  def get_timestamp(self):
    return str(datetime.datetime.now().timestamp())

  def info(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)