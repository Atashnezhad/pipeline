from astrapy.db import AstraDB
from dotenv import load_dotenv
import os


# Load .env file
load_dotenv()


if __name__ == "__main__":
    print("Hello World")

    # Now we can access the variables
    TOKEN = os.getenv("TOKEN")
    API_ENDPOINT = os.getenv("AOI_ENDPOINT")

    # Initialize the client
    db = AstraDB(token=TOKEN, api_endpoint=API_ENDPOINT)

    print(f"Connected to Astra DB: {db.get_collections()}")

    # Create a collection. The default similarity metric is "cosine".
    collection = db.create_collection("vector_test", dimension=5, metric="cosine")
    print(collection)

    # Insert documents into the collection
    documents = [
        {
            "_id": "1",
            "text": "ChatGPT integrated sneakers that talk to you",
            "$vector": [0.1, 0.15, 0.3, 0.12, 0.05],
        },
        {
            "_id": "2",
            "text": "An AI quilt to help you sleep forever",
            "$vector": [0.45, 0.09, 0.01, 0.2, 0.11],
        },
        {
            "_id": "3",
            "text": "A deep learning display that controls your mood",
            "$vector": [0.1, 0.05, 0.08, 0.3, 0.6],
        },
    ]
    res = collection.insert_many(documents)
    print(res)

    # Perform a similarity search
    query = [0.15, 0.1, 0.1, 0.35, 0.55]
    results = collection.vector_find(query, limit=2, fields={"text", "$vector"})

    for document in results:
        print(document)

    # Delete the collection
    res = db.delete_collection(collection_name="vector_test")
    print(res)
