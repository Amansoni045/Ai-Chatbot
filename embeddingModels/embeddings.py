# pyrefly: ignore [missing-import]
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


embeddings = OpenAIEmbeddings(model="text-embedding-ada-002",dimensions=64)

texts = [
    "Hello this is Aman Soni",
    "Hello my name is Aman",
    "I am a student",
    "I am a developer",
]

# vector = embeddings.embed_query("what is cricket?")
vector = embeddings.embed_documents(texts)

print(vector[0])