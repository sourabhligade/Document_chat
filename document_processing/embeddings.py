from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.db.mixins.sysdb import UniqueConstraintError

# Initialize the model and vector database
model = SentenceTransformer('all-MiniLM-L6-v2')  # Example model
client = chromadb.Client()

def create_collection(name='documents'):
    try:
        print(f"Attempting to create collection: {name}")
        client.create_collection(name=name)
        print(f"Collection '{name}' created successfully.")
    except UniqueConstraintError:
        print(f"Collection '{name}' already exists.")
    except Exception as e:
        print(f"Error creating collection '{name}': {e}")
        raise

def generate_embeddings(text):
    """
    Generate embeddings for the given text.
    """
    sentences = [text]  # In a real scenario, you might want to split text into sentences
    print(f"Generating embeddings for text: {text[:100]}...")  # Log only the first 100 characters for brevity
    embeddings = model.encode(sentences)
    print(f"Generated embeddings: {embeddings}")
    return embeddings

def store_embeddings(asset_id, embeddings):
    """
    Store embeddings in the vector database.
    """
    create_collection()
    collection = client.get_or_create_collection(name='documents')
    
    # Add the embeddings to the collection
    # The "documents" parameter should actually contain the original text or similar identifiers,
    # while embeddings can be stored in a separate structure if required by your design.
    collection.add(
        documents=[f"Document with ID {asset_id}"],  # Replace with the actual text or description
        ids=[asset_id],
        embeddings=embeddings.tolist()  # Add the embeddings separately if the API allows it
    )
    
    print("Embeddings stored successfully.")
