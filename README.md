# 📌 README.md

````markdown
# 🤖 LLM Powered Chatbot with Session History

This project is an **LLM-powered chatbot** built using [Streamlit](https://streamlit.io/) and [LangChain](https://www.langchain.com/), with integration to **Groq LLMs** via `langchain-groq`.  
It supports **chat history** (conversational memory) and provides an interactive web interface for users.

---

## 🚀 Features
- 🧠 Powered by **Groq LLMs** (`Gemma2-9b-It` in this project).  
- 💬 **Chat session history** using `st.session_state`.  
- 🎨 Streamlit-based UI with chat bubbles (`st.chat_message`).  
- 🔑 Secure handling of API keys via `.env` (local) or **Streamlit Secrets** (deployment).  
- 📓 Comes with both:
  - `1-chatbots.ipynb` → Notebook with LLM experiments.  
  - `app.py` → Deployable Streamlit chatbot app.  

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/YeshitaMotwani/LLM-Powered-Chatbot-with-Session-History.git
cd LLM-Powered-Chatbot-with-Session-History
````

Create a virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY_2="your_api_key_here"
```

⚠️ Do **not** commit `.env` to GitHub. It is already listed in `.gitignore`.

---

## ▶️ Running Locally

Run the chatbot locally with Streamlit:

```bash
streamlit run app.py
```

**Deployed on Streamlit:** https://llm-powered-chatbot-with-session-history.streamlit.app/

---

## 🌐 Deployment (Streamlit Cloud)

1. Push the repo to GitHub.
2. On [Streamlit Cloud](https://share.streamlit.io/), create a new app.
3. Select this repo and choose `app.py` as the entry point.
4. In **App Settings → Secrets**, add your API key in TOML format:

```toml
GROQ_API_KEY_2 = "your_api_key_here"
```

5. Deploy 🚀

---

## 📂 Project Structure

```
📦 LLM-Powered-Chatbot-with-Session-History
 ┣ 📜 app.py                # Streamlit chatbot app
 ┣ 📓 1-chatbots.ipynb      # Jupyter notebook for experiments
 ┣ 📜 requirements.txt      # Dependencies
 ┣ 📜 .gitignore            # Ignore .env and other unnecessary files
 ┗ 📜 README.md             # Project documentation
```

---

## 🧩 Tech Stack

* [Streamlit](https://streamlit.io/) → UI
* [LangChain](https://www.langchain.com/) → LLM framework
* [Groq LLMs](https://console.groq.com/) → Model provider
* [Python-dotenv](https://pypi.org/project/python-dotenv/) → Local env variable management

---

## ✨ Future Improvements

* 🔍 Add model selector (switch between different Groq models).
* 🗂️ Export chat history to text/CSV.
* 🧩 Add embeddings + vector store for knowledge-augmented chat.

---

## 👩‍💻 Author

**Yeshita Motwani**
📌 B.Tech CSE | Software Engineering Intern | AI & ML Enthusiast


