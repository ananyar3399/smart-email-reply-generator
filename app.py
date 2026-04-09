import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

# --- LangChain: Model wrapper ---
llm = ChatCohere(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    model="command-r-plus-08-2024",
    temperature=0.7
)

# --- ChatGPT Prompt Engineering: Structured system prompt ---
prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a professional email assistant. When given an email, generate exactly 3 reply options:
1. Formal – polished and professional
2. Neutral – friendly and clear
3. Brief – short and to the point

Label each reply clearly. Keep replies concise and relevant to the email's content.
If the user refers to a previous email in the conversation, use that context in your replies.
"""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# --- LangChain: Chain ---
chain = prompt | llm

# --- LangChain: Memory store ---
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# --- LangChain: Chain with memory ---
chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

def generate_replies(email_text):
    response = chain_with_memory.invoke(
        {"input": f"Here is the email I received:\n\n{email_text}"},
        config={"configurable": {"session_id": "user_session"}}
    )
    return response.content

if __name__ == "__main__":
    print("=== Smart Email Reply Generator ===")
    print("(Type 'quit' to exit | Memory is active — context carries across emails)\n")

    while True:
        print("Paste the email you received (then press Enter twice):\n")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            if line.lower() == "quit":
                print("Goodbye!")
                exit()
            lines.append(line)

        email_input = "\n".join(lines)
        if not email_input.strip():
            continue

        print("\nGenerating replies...\n")
        result = generate_replies(email_input)
        print(result)
        print("\n" + "="*50 + "\n")