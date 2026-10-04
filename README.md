# 🤖 Gemini AI Search Agent

An intelligent AI-powered search agent built with **Python** and the **Google Gemini API**. The agent can understand a user's query, decide when a web search is required, execute a search using **DuckDuckGo**, process the retrieved results, and generate a relevant response using Gemini.

This project demonstrates core **Agentic AI**, **Function Calling**, **Tool Execution**, **Multi-Step Reasoning**, and **Error Handling** concepts.

---

## 🚀 Features

* 🔎 Web search using DuckDuckGo
* 🤖 Gemini-powered intelligent responses
* 🧠 Agentic decision-making
* 🔧 Function/tool execution
* 🔄 Multi-step agent workflow
* 📊 Search result processing
* ⚠️ Error handling and retry mechanism
* ⏱️ Search timeout handling
* 🔐 Environment-variable based API key management
* 📝 Agent execution logs
* 🛠️ Configurable maximum steps and retries

---

## 🏗️ How It Works

The agent follows a simple workflow:

```text
User Query
    ↓
Gemini AI Agent
    ↓
Decide whether search is required
    ↓
Function Call: search()
    ↓
DuckDuckGo Web Search
    ↓
Search Results
    ↓
Gemini analyzes the results
    ↓
Final Answer
```

For example:

```text
User:
"What are the latest AI news today?"

        ↓

Agent:
Search is required

        ↓

search("latest AI news today")

        ↓

DuckDuckGo
        ↓
Search Results

        ↓

Gemini
        ↓

Final AI-generated answer
```

---

## 🧠 Agent Architecture

The project contains a custom search tool that allows Gemini to access current web information.

### Main Components

**1. Gemini Model**

Gemini is responsible for understanding the user's query, deciding whether a tool should be used, and generating the final response.

**2. Search Tool**

A custom Python `search()` function performs web searches using DuckDuckGo.

**3. Agent Loop**

The agent can perform multiple steps instead of immediately returning an answer.

**4. Error Handling**

The application handles API errors, search failures, timeouts, retries, and temporary service issues.

---

## 📁 Project Structure

```text
Gemini_Search_Agent/
│
├── agent.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .env
```

> ⚠️ The `.env` file should **never be uploaded to GitHub** because it contains your API key.

---

## 🛠️ Technologies Used

* **Python**
* **Google Gemini API**
* **DuckDuckGo Search**
* **python-dotenv**
* **HTTPX**
* **Agentic AI**
* **Function Calling**
* **Tool Execution**

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the project directory:

```bash
cd YOUR-REPOSITORY
```

---

### 2. Create a Virtual Environment

You can use your existing Anaconda environment or create a new Python virtual environment.

Using Anaconda:

```bash
conda create -n gemini_agent python=3.11
```

Activate it:

```bash
conda activate gemini_agent
```

---

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

The agent requires a **Google Gemini API key**.

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

The application loads the API key using `python-dotenv`.

### Example

```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
```

### ⚠️ Security

Never write your actual API key directly inside the Python source code.

Do **not** upload:

```text
.env
```

to GitHub.

Your `.gitignore` should contain:

```text
.env
__pycache__/
*.pyc
```

---

## ▶️ Running the Agent

After installing the dependencies and configuring your API key, run:

```bash
python agent.py
```

The agent will process the query and perform web searches when required.

---

## 🔎 Example Query

Example:

```text
What are the latest AI news today?
```

The agent can decide that current information is required and call the search tool.

Example workflow:

```text
[AGENT DECISION]
Search required

[FUNCTION CALL]
search(query="latest AI news today")

[TOOL EXECUTION]
Searching DuckDuckGo...

[TOOL RESULT]
5 search results returned

[AGENT]
Analyzing search results...

[FINAL ANSWER]
AI-related news based on the retrieved web results...
```

---

## 🔧 Search Function

The project includes a custom search function that uses DuckDuckGo.

Conceptually:

```python
def search(query):
    # Search the web
    # Retrieve relevant results
    # Return results to the agent
```

The search results contain useful information such as:

* Title
* URL
* Search snippet

These results are then provided to the Gemini agent for analysis.

---

## 🧩 Agentic Workflow

Unlike a simple chatbot, this project follows an agentic workflow.

### Step 1 — Understand

The agent receives the user's query.

### Step 2 — Decide

The agent determines whether it can answer directly or needs external information.

### Step 3 — Tool Selection

If web information is required, the agent selects the search tool.

### Step 4 — Tool Execution

The `search()` function searches DuckDuckGo.

### Step 5 — Process Results

The retrieved search results are passed back to the agent.

### Step 6 — Generate Answer

Gemini analyzes the available information and generates the final response.

### Step 7 — Continue if Needed

The agent can perform additional steps when necessary, subject to the configured maximum number of steps.

---

## 🔄 Error Handling

The application includes error-handling mechanisms for common runtime problems.

These include:

* API errors
* Temporary service failures
* Search errors
* Request timeouts
* Rate-limit/quota issues
* Retryable failures

The agent uses configurable retry behavior to improve reliability.

Example configuration:

```python
MAX_STEPS = 6
MAX_RETRIES = 4
SEARCH_TIMEOUT = 20
```

These values can be adjusted depending on the application requirements.

---

## 📝 Logging

The agent provides execution logs to make the workflow easier to understand and debug.

Example:

```text
[AGENT DECISION]
[FUNCTION CALL]
[TOOL EXECUTION]
[TOOL RESULT]
```

These logs help track:

* What the agent decided
* Which function it called
* When the tool was executed
* What result the tool returned

---

## 💡 Why This Project?

This project was developed to understand and implement practical concepts in **Agentic AI**.

Instead of building a chatbot that only generates text, the project demonstrates how an AI model can:

```text
Reason
   ↓
Choose a Tool
   ↓
Execute the Tool
   ↓
Receive Information
   ↓
Reason Again
   ↓
Generate Final Response
```

This approach is useful for building more capable AI applications that can interact with external tools and information sources.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* Gemini API integration
* Agentic AI architecture
* Function calling concepts
* Tool execution
* Web search integration
* Multi-step reasoning
* API error handling
* Retry mechanisms
* Timeout management
* Environment variables
* Secure API key management
* Python-based AI application development

---

## 🧪 Testing

The agent was tested with different types of queries, including queries that require current web information.

Example:

```text
"Top news of today about AI?"
```

The agent successfully:

1. Identified that current information was required.
2. Called the search function.
3. Retrieved multiple DuckDuckGo results.
4. Returned the results to the agent.
5. Generated a response based on the retrieved information.

---

## 🔐 Security Notes

Keep API credentials private.

Never commit:

```text
.env
```

or any file containing:

```text
GEMINI_API_KEY
```

Use environment variables instead.

A recommended `.gitignore`:

```text
.env
__pycache__/
*.pyc
.vscode/
```

---

## 📋 Requirements

The main dependencies used by this project include:

```text
google-genai
ddgs
python-dotenv
httpx
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

Possible improvements include:

* Adding more external tools
* Supporting additional search providers
* Adding a Streamlit user interface
* Adding conversation memory
* Adding source citations in the final response
* Implementing more advanced planning strategies
* Adding structured tool schemas
* Adding persistent conversation history
* Improving search-result ranking
* Adding automated evaluation tests

---

## 👩‍💻 Author

**Laiba Aamer**

BS Artificial Intelligence Student

Interested in:

* Artificial Intelligence
* Machine Learning
* Generative AI
* Agentic AI
* Data Science
* AI Application Development

---

## ⭐ Project Highlights

This project demonstrates a practical implementation of an AI agent that combines:

```text
Gemini
+
Web Search
+
Function Calling
+
Tool Execution
+
Agentic Reasoning
+
Error Handling
```

It serves as a foundation for building more advanced **AI agents and tool-using LLM applications**.

---

## 📄 License

This project is intended for educational and portfolio purposes.

