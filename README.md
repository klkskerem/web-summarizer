# Web Summarizer

A modular and lightweight web summarization tool powered by Large Language Models (LLMs). The project crawls web pages, extracts clean readable content by stripping HTML boilerplate, and generates structured summaries using either local open-source models or cloud-based AI providers via a unified interface.

## Features

- **Web Scraping & Cleaning:** Extracts human-readable text from target web pages using `requests` and `BeautifulSoup4`, discarding scripts, styles, and boilerplate navigation markup.
- **Unified LLM Interface:** Utilizes the OpenAI-compatible SDK to seamlessly toggle between local and cloud providers with a single configuration flag.
- **Dual Provider Support:**
  - **Local:** Ollama (e.g., `llama3.2`) for offline, cost-free, and privacy-preserving execution.
  - **Cloud:** Google Gemini (e.g., `gemini-3.8-flash` / `gemini-2.5-flash`) for cloud-scale speed and reasoning.
- **Environment Security:** Manages secrets and API keys securely through `.env` and `.gitignore`.



## Architecture & Tech Stack

- **Language:** Python 3.10+
- **HTTP & Parsing:** `requests`, `beautifulsoup4`
- **LLM Integration:** `openai` SDK (used as a universal client)
- **Environment Management:** `python-dotenv`



## Getting Started



### 1. Prerequisites

- Python installed on your system.
- (Optional) [Ollama](https://ollama.com/) running locally if using local inference:

```bash
ollama run llama3.2
```



### 2. Installation

- Clone the repository and install the dependencies:

```bash
git clone https://github.com/klkskerem/web-summarizer.git
cd web-summarizer
pip install -r requirements.txt
```



### 3. Environment Setup

- Create a .env file in the root directory (do not commit this file to version control):

```bash
GEMINI_API_KEY=your_actual_gemini_api_key_here
```



### 4. Configuration & Usage

- Open main.py and set your preferred provider:

```bash
# Set to True for local Ollama, or False for Google Gemini
USE_OLLAMA = True
```

- Run the application:

```bash
python main.py
```



## License

This project is open-source and available under the MIT License.