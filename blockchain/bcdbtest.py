class Block:
    id = None
    history = None
    parent_id = None
block_A = Block()
block_A.id = 1
block_A.history = 'Nelson likes cat'
block_B = Block()
block_B.id = 2
block_B.history = 'Marie likes dog'
block_B.parent_id = block_A.id
block_C = Block()
block_C.id = 3
block_C.history = 'Sky hates dog'
block_C.parent_id = block_B.id
print(f"Block A: id={block_A.id}, history='{block_A.history}', parent_id={block_A.parent_id}")
print(f"Block B: id={block_B.id}, history='{block_B.history}', parent_id={block_B.parent_id}")
print(f"Block C: id={block_C.id}, history='{block_C.history}', parent_id={block_C.parent_id}")

