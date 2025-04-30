from pymilvus import Collection, connections

# Connect to Milvus
connections.connect()

# Load the collection
collection = Collection("example_collection")

# Define index parameters
index_params = {
    "index_type": "IVF_FLAT",  # Example index type
    "metric_type": "L2",       # Distance metric (e.g., L2 for Euclidean)
    "params": {"nlist": 128}   # Index-specific parameters
}

# Create the index for the collection
collection.create_index(field_name="your_vector_field_name", index_params=index_params)

# Optionally, load the collection after the index is created
collection.load()

