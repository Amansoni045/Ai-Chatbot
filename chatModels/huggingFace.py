import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# Set HUGGINGFACEHUB_API_TOKEN from .env if present
if "HUGGINGFACEHUB_ACCESS_TOKEN" in os.environ:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"]

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("who are you?")

print(response.content)