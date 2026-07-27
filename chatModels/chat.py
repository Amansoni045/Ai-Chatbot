from dotenv import load_dotenv

load_dotenv()

# from langchain.chat_models import init_chat_model 

# model = init_chat_model("llama-3.3-70b-versatile",model_provider="groq")

# from langchain_openai import ChatOpenAI

# model = ChatOpenAI(model = "gpt-5")

# response = model.invoke("what is cricket?")

# print(response.content) 

# from langchain.chat_models import init_chat_model 

# model = init_chat_model("groq/compound-mini",model_provider="groq")

from langchain_groq import ChatGroq

model = ChatGroq(model="llama-3.3-70b-versatile")

response = model.invoke("what is cricket?")

print(response.content)

#same we can do for mistral, gemini and all other models

#we can also set the temperature of the model so that it can get more creative or for more specific answer 

#we can also set max_tokens so that we can get the response of the model in the specific number of words


