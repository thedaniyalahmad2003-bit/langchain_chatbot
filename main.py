# from langchain_ollama import ChatOllama

# llm=ChatOllama(
#     model="qwen2.5:3b",
#     temperature=0.3
#     )

# response = llm.invoke("What is AI?")
# print(response.content)





# from langchain_ollama import ChatOllama
# from langchain_core.messages import SystemMessage, HumanMessage

# llm=ChatOllama(
#     model="qwen2.5:3b",
#     temperature=0.3
#     )

# messages=[
#     SystemMessage(content="You are a helpful assistant."),
#     HumanMessage(content="What is AI?")
# ]

# response = llm.invoke(messages)
# print(response.content)




# from langchain_ollama import ChatOllama
# from langchain_core.prompts import ChatPromptTemplate

# llm=ChatOllama(
#     model="qwen2.5:3b",
#     temperature=0.3
#     )

# prompt=ChatPromptTemplate.from_messages([
#     ("system", "You are a expert in {topic}."),
#     ("human", "{question}")
# ])

# chain= prompt | llm
# response = chain.invoke({"topic": "geography", "question": "capital of france?"})
# print(response.content)




from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=ChatOllama(
    model="qwen3.5:0.8b",
    temperature=0.3
    )

prompt=ChatPromptTemplate.from_messages([
    ("system", "You are a expert in {topic}."),
    ("human", "{question}")
])

chain= prompt | llm | StrOutputParser()

for chunk in chain.stream({"topic": "geography", "question": "capital of france?"}):
    print(chunk, end="", flush=True)