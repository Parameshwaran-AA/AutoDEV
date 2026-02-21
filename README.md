Below is the System Architecture 

Client (API Request)
        ↓
FastAPI Backend
        ↓
AutoDev Orchestrator
        ↓
-------------------------------------------------
| Planner → Architect → Coder → Tester         |
|             ↓                                 |
|         Debugger (if failed)                 |
|             ↓                                 |
|          Refactor Agent                      |
-------------------------------------------------
        ↓
Tool Layer (FS, Git, Test, Lint, Docker)
        ↓
Memory Layer (Vector Store + DB)







