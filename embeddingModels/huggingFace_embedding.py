from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()


embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

texts = [
    "Hello this is Aman Soni",
    "Hello my name is Aman",
    "I am a student",
    "I am a developer",
]

vector = embedding.embed_documents(texts)

print(vector[0])