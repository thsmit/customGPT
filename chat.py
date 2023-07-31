import os
import sys

# import APIKEY
import key

# langchain imports
from langchain.document_loaders import PyPDFLoader 
from langchain.embeddings import OpenAIEmbeddings 
from langchain.vectorstores import Chroma 
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

# set the OpenAI API key
os.environ["OPENAI_API_KEY"] = key.APIKEY

## load PDF's in /data
loader = PyPDFLoader("./data/bitcoin_paper.pdf")
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(pages, embedding=embeddings, persist_directory=".")
db.persist()

# log the conversation
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# create our Q&A chain
qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.8) , db.as_retriever(), memory=memory)

yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;39m"

#chat_history = []
print(f"{yellow}---------------------------------------------------------------------------------")
print('Welcome to the customGPT. You are now ready to start interacting with your documents')
print('---------------------------------------------------------------------------------')

while True:
    query = input(f"{green}Prompt: ")
    if query == "exit" or query == "quit" or query == "q" or query == "f":
        print('Exiting')
        sys.exit()
    if query == '':
        continue
    result = qa({"question": query})
    #result = qa({"question": query, "chat_history": chat_history})

    print(f"{white}Answer: " + result["answer"])
    #chat_history.append((query, result["answer"]))