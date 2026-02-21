# AutoDevX — Autonomous Multi-Agent AI Software Engineering System

AutoDevX is a production-oriented multi-agent AI system that transforms high-level product requirements into structured implementation plans, architecture designs, executable code, automated tests, and refactored outputs.

The goal of this project is to simulate an AI-driven engineering workflow that mirrors how a real software team operates — planner, architect, developer, QA, and reviewer — coordinated through a unified orchestration layer.

This project was built to demonstrate advanced capabilities in:

- AI agent orchestration
- Backend system design
- Production-grade Python development
- Tool-augmented LLM systems
- Containerized deployment

---

## Why This Project

Most AI projects stop at simple chatbots or RAG systems.

AutoDevX goes further by:

- Coordinating multiple specialized agents
- Executing generated code
- Running automated tests
- Detecting failures
- Attempting self-correction
- Refactoring and improving outputs
- Integrating development tools (pytest, flake8, Docker, Git)

The system is designed to reflect real-world software engineering workflows rather than isolated prompt-response interactions.

---

## System Overview

At a high level, the workflow looks like this:

1. A user submits a product requirement.
2. The **Planner Agent** breaks it into implementation steps.
3. The **Architect Agent** proposes a structured system design.
4. The **Coder Agent** generates production-ready Python code.
5. The **Tester Agent** writes pytest-based unit tests.
6. Tests are executed automatically.
7. If tests fail, the **Debugger Agent** analyzes failures and regenerates fixes.
8. The **Refactor Agent** improves structure, readability, and quality.
9. Results are returned through a FastAPI interface.

The system is built in a modular way so that new agents and tools can be added easily.

---

## Architecture

**Core Components:**

- FastAPI backend
- Custom multi-agent orchestration engine
- Tool layer (file system, testing, linting, Docker)
- PostgreSQL for persistent state
- Redis for future async task orchestration
- FAISS vector store for memory (extensible)
- Dockerized deployment

The architecture follows clear separation of concerns:

- Agents focus on reasoning
- Tools handle execution
- Orchestrator manages control flow
- API layer exposes functionality

---

## Tech Stack

- Python 3.11+
- FastAPI
- OpenAI API (LLM reasoning)
- PostgreSQL
- Redis
- FAISS
- Pytest
- Flake8
- Docker & Docker Compose
- GitPython

---

## Project Structure

```
autodevx/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── api/
│   ├── agents/
│   ├── tools/
│   ├── memory/
│   └── models/
│
├── docker/
│   └── Dockerfile
│
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

The project is organized to reflect production-ready modular design rather than a single-script prototype.

---

## Running the Project

### 1. Create Environment File

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key_here
DATABASE_URL=postgresql://postgres:postgres@db:5432/autodevx
REDIS_URL=redis://redis:6379
```

> Do not commit this file. Add `.env` to `.gitignore`.

### 2. Run with Docker (Recommended)

From the project root:

```bash
docker-compose up --build
```

Once running, access:

```
http://localhost:8000/docs
```

You can test the `/generate` endpoint from the Swagger UI.

### 3. Run Locally (Development Mode)

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start server:

```bash
uvicorn app.main:app --reload
```

---

## Example Usage

Send a POST request to `/generate`:

```json
{
  "description": "Build a REST API for managing tasks with CRUD operations"
}
```

The system will return:

- Implementation plan
- Proposed architecture
- Generated code
- Generated tests
- Refactoring output

---

## Engineering Highlights

- Abstract base agent pattern
- Async-ready backend design
- Structured orchestration flow
- Self-correction loop for failing tests
- Tool-augmented LLM usage
- Containerized environment isolation
- Clear separation of reasoning and execution layers

---

## Future Enhancements

Planned improvements include:

- Iterative retry loops with bounded correction attempts
- GitHub pull request automation
- CI/CD integration
- Observability and structured logging
- Cloud deployment (AWS/GCP)
- Authentication layer
- Background task queue (Celery)

---

## Purpose

This project was built to demonstrate practical implementation of:

- AI agent systems
- Production backend architecture
- Software engineering best practices
- Tool-integrated LLM workflows

It reflects real-world AI engineering challenges rather than simplified demos.

---

## Author

**Parameshwaran**  
AI Engineer | Software Systems | Agent Architecture
