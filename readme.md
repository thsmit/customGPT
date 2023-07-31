# CustomGPT

## Environment 

'''
conda activate customGPT
'''

## Just test it

Using local data only (data.txt):

```
python test.py "Who was the first president of the USA?"
python test.py "What is the birthday of X?"
```

## Just test it with a PDF

Using local data only from a PDF:

```
python chat.py "Who was the first president of the USA?"
python chat.py "What is Bitcoin?"
```

## Good to know

There is a token limit on the amount of custom data we can send to chatGPT to get processed and ask questions about it. Therefore, we have to select 'revelant' information out of our custom data base and send only the relevant information to chatGPT. Selecting the relevant information is done via 'Embeddings'. The embeddings transformer is categorizing all the custom text. This allowes to only use the releavant category of custom text based on the question asked.

Embeddings are stored in a Vectorstore.

## Sources

On langchain:

https://github.com/hwchase17/langchain

Example reading a PDF:

https://levelup.gitconnected.com/chatgpt-for-pdf-files-with-langchain-ef565c041796