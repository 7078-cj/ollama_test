from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from RAG.vector import retriever

model = OllamaLLM(model='gemma3:4b')

template = """
    You are an expert in answering questions about a pizza restaurant
    
    Here are some relevant reviews: {reviews}
    
    Here is the question to answer: {question}
    
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print('-----------------------------------------')
    question = input("ask your question (q to quit): ")
    if question == 'q':
        break
    
    print('-----------------------------------------')
    reviews = retriever.invoke(question)
    result = chain.invoke({
                    'reviews':reviews, 
                    'question':question
                })

    print(result)