from block import Block
from blockchain import Blockchain
from config import *
import random
import json

bc = Blockchain()

bc.add_block(
  Block(
    index = 1,
    data_dict = { 'token': random.randint(0,1000)  }
  )
)

bc.add_block(
  Block(
    index = 2,
    data_dict = { 'token': random.randint(0,1000)  }
  )
)

bc.add_block(
  Block(
    index = 3,
    data_dict = { 'token': random.randint(0,1000)  }
  )
)

print("Is valid blockchain -> " + str(bc.chain_validator()))

for c in bc.chain:
  print(c.info())

