from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st

# -----------------------------------
# Load Environment Variables
# -----------------------------------
load_dotenv()

# -----------------------------------
# Streamlit Page Config
# MUST BE THE FIRST STREAMLIT COMMAND
# -----------------------------------
st.set_page_config(
    page_title="🤖 Daily AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# Initialize Chat History
# -----------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

# -----------------------------------
# Custom CSS
# -----------------------------------
st.markdown("""
<style>

.stApp{
    background-color:#0E1117;
}

.block-container{
    max-width:900px;
    padding-top:2rem;
}

.chat-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    background:linear-gradient(90deg,#4facfe,#00f2fe);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    text-align:center;
    color:#BBBBBB;
    margin-bottom:25px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Load Model
# -----------------------------------
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# -----------------------------------
# Sidebar
# -----------------------------------
with st.sidebar:

    st.title("🤖 AI Chatbot")

    st.success("🟢 Model Connected")

    st.divider()

    st.subheader("Features")

    st.markdown("""
-  Multi-turn Chat
-  Conversation Memory
-  DeepSeek V4 Pro
-  LangChain
""")

    st.divider()

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.chat_history = [
            SystemMessage(content="You are a helpful AI assistant.")
        ]
        st.rerun()

    st.divider()

    message_count = sum(
        isinstance(msg, (HumanMessage, AIMessage))
        for msg in st.session_state.chat_history
    )

    st.caption(f"💬 Messages : {message_count}")

# -----------------------------------
# Title
# -----------------------------------
st.markdown("""
<div class="chat-title">
🤖 Daily AI Chatbot
</div>

<div class="subtitle">
Powered by DeepSeek V4 Pro • LangChain 
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# Welcome Message
# -----------------------------------
if len(st.session_state.chat_history) == 1:
    st.info(" Welcome! Ask me anything.")

# -----------------------------------
# Display Chat
# -----------------------------------
for message in st.session_state.chat_history:

    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message.content)

st.divider()

# -----------------------------------
# Chat Input
# -----------------------------------
user_input = st.chat_input("Type your message...")

if user_input:

    # Show User Message
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    # Store User Message
    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )

    # Generate AI Response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("🤖 Thinking..."):
            response = model.invoke(st.session_state.chat_history)
            st.markdown(response.content)

    # Store AI Response
    st.session_state.chat_history.append(
        AIMessage(content=response.content)
    )
