# 🤖 Daily AI Chatbot

A conversational AI chatbot built using **LangChain**, **Hugging Face**, **DeepSeek-V4-Pro**, and **Streamlit**. This project provides a clean chat interface with conversation memory and serves as the foundation for a more advanced AI assistant.

> **⚠️ Note:** This project is currently under active development. I will continue improving it by adding new features, optimizing performance, and experimenting with advanced LLM capabilities.

---

## 🚀 Features

- 💬 Interactive chat interface built with Streamlit
- 🧠 Conversation memory using LangChain message history
- 🤖 Powered by DeepSeek-V4-Pro through Hugging Face Inference API
- ⚡ Clean and responsive UI
- 🔄 Maintains context throughout the conversation
- 🌐 Environment variable support using `.env`

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Hugging Face Inference API
- DeepSeek-V4-Pro
- python-dotenv


## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/DeepSeek-AI-Chatbot.git
cd DeepSeek-AI-Chatbot
```

### Create a virtual environment (Recommended)

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Preview

<img width="941" height="897" alt="Screenshot 2026-07-22 145001" src="https://github.com/user-attachments/assets/e720f5a3-ed4d-4cd9-80cf-0fb7046e155d" />


---

## 📌 Current Functionality

- Chat with DeepSeek-V4-Pro
- Multi-turn conversation support
- Chat history maintained using Streamlit Session State
- User-friendly chat interface

---

# 🚧 Roadmap

This project is **far from complete**. My goal is to continuously improve it and transform it into a much more capable AI assistant.

Some planned features include:

- [ ] Streaming responses
- [ ] Chat history export
- [ ] Dark/Light mode support
- [ ] Multiple LLM support
- [ ] Prompt templates
- [ ] Conversation management
- [ ] File upload support
- [ ] PDF Question Answering (RAG)
- [ ] Web Search integration
- [ ] Memory optimization
- [ ] Voice input
- [ ] Voice output
- [ ] Multi-agent workflows
- [ ] Research Paper Assistant
- [ ] Citation generation
- [ ] Authentication
- [ ] Database support
- [ ] Deployment

---

## 🎯 Future Vision

This chatbot is the starting point of a larger learning journey into **Generative AI** and **LLM Engineering**.

I plan to keep contributing to this repository regularly by:

- Exploring new LangChain features
- Integrating advanced Retrieval-Augmented Generation (RAG)
- Improving reasoning and response quality
- Enhancing the user interface and user experience
- Experimenting with agentic AI workflows
- Building features inspired by real-world AI assistants

The objective is to gradually evolve this project from a basic chatbot into a robust, feature-rich AI assistant.

---

## 🤝 Contributions

Suggestions, issues, and feature requests are always welcome.

If you have ideas that could improve this project, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

### ⭐ If you found this project interesting, consider giving it a star!
