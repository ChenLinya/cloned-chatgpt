from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key,
                       openai_api_base="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input":prompt})
    return response["response"]

# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("世界上最高的地方是哪里？",memory,"sk-liaIeosjNGlmc925271a4c237aC04d0eAa1fF1F53fC41655"))
# print(get_chat_response("最深的呢？",memory,"sk-liaIeosjNGlmc925271a4c237aC04d0eAa1fF1F53fC41655"))
