# Kansai Dialect Agent Server

This project implements an AI agent server that communicates in the Kansai dialect of Japanese. It utilizes the `a2a-server` framework, Google Agent Development Kit (`google-adk`), LiteLLM, and a Google Gemini model.

## Features

*   Responds to prompts in Kansai dialect (Kansai-ben).
*   Built using the `a2a-server` and `google-adk` libraries.
*   Uses LiteLLM to interact with the Gemini LLM.
*   Configurable via `agent.yaml`.

## Requirements

*   Python >= 3.13
*   `uv` package manager (recommended)
*   A Google Gemini API Key

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd test
    ```

2.  **Set up virtual environment and install dependencies:**
    ```bash
    # Create and activate virtual environment (using uv)
    uv venv
    source .venv/bin/activate 
    
    # Install dependencies
    uv pip install -r requirements.txt  # Or potentially: uv sync
    ```
    *Note: Dependencies are managed via `pyproject.toml` and locked in `uv.lock`.*

3.  **Configure Environment Variables:**
    Copy the example environment file and add your API key:
    ```bash
    cp .env.example .env
    ```
    Now, edit the `.env` file and replace `YOUR-GEMINI-API-KEY` with your actual Gemini API key.

## Running the Server

Ensure your virtual environment is activated (`source .venv/bin/activate`).

Start the server using:

```bash
python kansai/main.py
```

The server will start, typically on `http://localhost:8000` (as configured in `agent.yaml`).

## Configuration

The agent's behavior, server port, and metadata are configured in `agent.yaml`.

## Dependencies

*   `a2a-server`: Framework for building agent servers.
*   `google-adk`: Google Agent Development Kit.
*   `litellm`: Library for interacting with various LLMs.
*   `python-dotenv`: For loading environment variables from a `.env` file.