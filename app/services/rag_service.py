from pinecone import Pinecone, ServerlessSpec
from app.config import PINECONE_API_KEY

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "chat-memory"

# Create index if not exists
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # embedding size
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(index_name)


# 🔹 Simple embedding (lightweight)
def simple_embedding(text):
    # Convert text → numeric vector (lightweight trick)
    return [float(ord(c)) for c in text[:384]] + [0.0] * (384 - len(text[:384]))


def store_message(user_id, message):
    vector = simple_embedding(message)

    index.upsert([
        (f"{user_id}-{hash(message)}", vector, {"text": message})
    ])


def retrieve_context(query, top_k=3):
    vector = simple_embedding(query)

    results = index.query(
        vector=vector,
        top_k=top_k,
        include_metadata=True
    )

    return [match["metadata"]["text"] for match in results["matches"]]