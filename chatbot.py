from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Streamlit Page Configuration
st.set_page_config(
    page_title="Daily AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize Model
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

st.title("🤖 Daily AI Chatbot")
st.caption("Powered by Hugging Face + LangChain")

# Display Previous Messages
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# User Input
user_input = st.chat_input("Type your message...")

if user_input:

    # Show User Message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Save User Message
    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )

    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.chat_history)

            st.markdown(response.content)

    # Save AI Response
    st.session_state.chat_history.append(
        AIMessage(content=response.content)
    )