# Kansai Dialect Agent Server

This project implements an AI agent server that communicates in the Kansai dialect of Japanese. It utilizes the `a2a-server` framework, Google Agent Development Kit (`google-adk`), LiteLLM, and a Google Gemini model.

Thanks a lot Chris Hay for his easy to understand explanation.
This code based on his code base, please go check:
https://github.com/chrishayuk/a2a-server

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
    uv init
    
    # Install dependencies
    uv add a2a-server
    uv add google-adk
    uv add litellm
    uv add python-dotenv
    ```
    *Note: Dependencies are managed via `pyproject.toml` and locked in `uv.lock`.*

3.  **Configure Environment Variables:**
    Copy the example environment file and add your API key:
    ```bash
    cp .env.example .env
    ```
    Now, edit the `.env` file and replace `YOUR-GEMINI-API-KEY` with your actual Gemini API key.

## Running the Server

Start the server using:

```bash
uv run -m a2a_server --config agent.yaml 
```

The server will start, typically on `http://localhost:8000` (as configured in `agent.yaml`).

## Using CLI

After starting the server, use:

```bash
uvx a2a-cli
```

## Configuration

The agent's behavior, server port, and metadata are configured in `agent.yaml`.

## Dependencies

*   `a2a-server`: Framework for building agent servers.
*   `google-adk`: Google Agent Development Kit.
*   `litellm`: Library for interacting with various LLMs.
*   `python-dotenv`: For loading environment variables from a `.env` file.
