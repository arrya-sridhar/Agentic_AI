# Agentic_AI
Basic steps towards building agentic ai 

This repository contains:

- **Level 1**: Basic LLM calls, PDF analysis and an user interface that combines both the functions
- **Level 2**: FastMCP weather tool server and client with Google Gemini

It uses:
- Google Gemini , model = gemini-2.5-flash
- OpenWeather API for weather retrieval 

## Setup & Run

1. **Clone the repository**  
```
git clone https://github.com/arrya-sridhar/Agentic_AI.git
cd Agentic_AI/LYNQtasks
```

2. **Level 1**  
- Create and activate a virtual environment:  
  ```
  cd level1
  python3 -m venv venv
  source venv/bin/activate    # Windows: venv\Scripts\activate
  ```
- Install dependencies and set API key:  
  ```
  pip install -r requirements.txt
  export GOOGLE_API_KEY=your_gemini_api_key_here
  ```
- Run scripts:  
  ```
  python step1.py
  python step2.py
  python app.py
  ```

3. **Level 2**  
- Create and activate a virtual environment:  
  ```
  cd ../level2
  python3 -m venv venv
  source venv/bin/activate
  ```
- Install dependencies and set API key:  
  ```
  pip install -r requirements.txt
  export GOOGLE_API_KEY=your_gemini_api_key_here
  export OPENWEATHER_API_KEY=your_openweather_api_key_here
  ```
- Start MCP server (Terminal 1):  
  ```
  python weather_mcp.py
  ```
- Run client agent (Terminal 2):  
  ```
  python client_agent.py
  ```

---

**Note:** Exporting API keys are temporary and needs to be done for every new shell.
