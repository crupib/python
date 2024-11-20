from pymilvus import connections, Collection, utility

# 1. Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# 2. Define the collection name
collection_name = "example_collection"

# 3. Check if the collection exists (optional)
if utility.has_collection(collection_name):
    print(f"Collection '{collection_name}' exists. Dropping the collection...")
    
    # 4. Drop the collection
    collection = Collection(collection_name)
    collection.drop()

    # 5. Verify if the collection has been dropped
    if not utility.has_collection(collection_name):
        print(f"Collection '{collection_name}' has been successfully removed.")
else:
    print(f"Collection '{collection_name}' does not exist.")

