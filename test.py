import os
import sys

import key

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = key.APIKEY

# Obtain the user query from command-line arguments
query = sys.argv[1]
print('Query...: ', query)

# Load the personal data
loader = TextLoader('./data/data.txt')

# Create an index for the loaded data
index = VectorstoreIndexCreator().from_loaders([loader])

# use for Default behaviour: index.query(query)) = using personal data only!
print('Awnser...: ', index.query(query))

#from langchain.chat_models import ChatOpenAI
#print('Awnser...: ', index.query(query, llm=ChatOpenAI()))