from block import Block
import random

class Blockchain:

  def __init__(self):
    self.chain = []
    self.chain.append(self.create_block())

  def create_block(self):
    return Block(
      index = 0,
      data_dict = { 'token': random.randint(0,1000)  },
      previous_hash = ''
    )

  def get_current_block(self):
    return self.chain[-1]

  def add_block(self, block):
    block.previous_hash = self.get_current_block().hash
    self.chain.append(block)

  def chain_validator(self):
    chain = self.chain
    for i in range(len(chain)):
      if i == 0: continue

      current_block = chain[i]
      previous_block = chain[i-1]

      if current_block.previous_hash != previous_block.hash:
        return False
      
    return True