# 📧 Smart Email Reply Generator

An AI-powered tool that generates 3 contextually appropriate email reply options — **formal**, **neutral**, and **brief** — from any email you paste. Built with **LangChain** and **Cohere**, featuring conversation memory that carries context across emails in the same session.

Built as a hands-on project combining concepts from two DeepLearning.AI courses:
- ✅ ChatGPT Prompt Engineering for Developers
- ✅ LangChain for LLM Application Development

---

## 🚀 Demo

```
=== Smart Email Reply Generator ===
(Type 'quit' to exit | Memory is active — context carries across emails)

Paste the email you received (then press Enter twice):

Hi, I wanted to follow up on the job application I submitted last week.
Could you let me know the current status?

Generating replies...

1. Formal:
Thank you for reaching out. We have received your application and it is currently under review.
We will be in touch with you shortly regarding the next steps.

2. Neutral:
Thanks for following up! Your application is still being reviewed and we'll get back to you
as soon as we have an update.

3. Brief:
Thanks for checking in! Still under review — will update you soon.
```

---

## 🧠 Concepts Applied

### From ChatGPT Prompt Engineering for Developers
- Structured **system prompt** design to control tone and output format
- **Iterative prompt refinement** to get consistent 3-reply structure
- Controlling model behaviour through prompt design alone

### From LangChain for LLM Application Development
- `ChatPromptTemplate` for reusable, structured prompts
- `MessagesPlaceholder` for injecting memory into the prompt
- `InMemoryChatMessageHistory` for conversation memory
- `RunnableWithMessageHistory` to chain model + prompt + memory

---

## 🛠️ Tech Stack

- **Python** 3.x
- **LangChain** – prompt templates, memory, chains
- **Cohere API** – LLM backend (`command-r-plus-08-2024`)
- **python-dotenv** – environment variable management

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/ananyar3399/smart-email-reply-generator.git
cd email-reply-generator
```

### 2. Install dependencies
```bash
pip install langchain langchain-cohere langchain-core cohere python-dotenv
```

### 3. Get a free Cohere API key
- Sign up at [dashboard.cohere.com](https://dashboard.cohere.com)
- Copy your API key from the dashboard (no credit card required)

### 4. Create a `.env` file
```
COHERE_API_KEY=your_cohere_api_key_here
```

### 5. Run the app
```bash
python app.py
```

---

## 📁 Project Structure

```
smart-email-reply-generator/
│
├── app.py          # Main application
├── .env            # API key (never commit this)
├── .gitignore      # Excludes .env from git
└── README.md       # You're here
```

---

## 🔒 Important

Never upload your `.env` file to GitHub. Make sure your `.gitignore` contains:
```
.env
```

---

## 📚 Courses Referenced

- [ChatGPT Prompt Engineering for Developers – DeepLearning.AI](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- [LangChain for LLM Application Development – DeepLearning.AI](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)

---

## 👩‍💻 Author

Built by Ananya as a hands-on alternative to paid course certificates.
