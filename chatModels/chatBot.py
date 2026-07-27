from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(model="open-mistral-7b")

print("choose your ai mode")
print("press 1 for Sad AI agent")
print("press 2 for Happy AI agent")
print("press 3 for Angry AI agent")
print("press 4 for Romantic AI agent")

choice = int(input("tell your response:- "))

if(choice == 1):
    messages = [SystemMessage(content="you are a Sad AI agent and reply every message in sad way")]
elif(choice == 2):
    messages = [SystemMessage(content="you are a Happy AI agent and reply every message in happy way")]
elif(choice == 3):
    messages = [SystemMessage(content="you are a Angry AI agent and reply every message in angry way")]
elif(choice == 4):
    messages = [SystemMessage(content="you are a Romantic AI agent and reply every message in romantic way")]

while True:
    print("----------------Welcome type 0 to exit the application------------")
    prompt = input("YOU : ")

    messages.append(HumanMessage(content=prompt))

    if prompt == "0":
        break

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("MISTRAL : ",response.content)

print(messages)