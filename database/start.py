from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection
import numpy as np

# 1. Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# 2. Define schema
fields = [
    FieldSchema(name="ID", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=128)
]
schema = CollectionSchema(fields, description="A collection to store vector embeddings")

# 3. Create collection
collection = Collection(name="example_collection", schema=schema)

# 4. Insert data
num_entities = 10
vectors = np.random.random((num_entities, 128)).astype(np.float32)
collection.insert([vectors])

# 5. Create index
index_params = {"index_type": "IVF_FLAT", "params": {"nlist": 128}, "metric_type": "L2"}
collection.create_index(field_name="embeddings", index_params=index_params)

# 6. Load collection
collection.load()

# 7. Search
query_vector = np.random.random((1, 128)).astype(np.float32)
search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
results = collection.search(query_vector, "embeddings", search_params, limit=5)

# 8. Display results
for result in results:
    print(f"ID: {result.ids}, Distance: {result.distances}")

