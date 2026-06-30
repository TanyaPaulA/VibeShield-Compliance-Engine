# VibeShield Compliance Engine

VibeShield is a local repository assistant framework powered by Model Context Protocol (MCP) and a deterministic state-graph routing engine. The system analyzes local repository modifications or file deltas, automatically generates structured, professional documentation updates (such as README components) and clean Git commit messages, and validates them against strict local style guide parameters before file synchronization.

---

## Core Features

* **Automated Documentation & Commit Generation:** Reviews ongoing development changes and automatically constructs precise technical documentation segments and standardized Git commit messages.
* **Deterministic State Graph Routing (`app/agent.py`):** Directs the lifecycle of repository processing from ingestion and evaluation through error containment and termination tracks.
* **Structural Workspace Validation (`app/validator.py`):** Acts as a structural quality check by parsing template files to ensure no unverified placeholder text strings or structural discrepancies exist.
* **Self-Healing Layout Correction:** Intercepts compliance failures programmatically, deploying disk-level automated file patching to correct malformed markdown files.
* **Zero-Cost Local Architecture:** Utilizes local MCP filesystem configurations to operate directly on the user's workstation with no external cloud servers or API subscription fees.

---
### Component Matrix

| System Layer | Operational Mode | Targeted Artifacts | Infrastructure Cost |
| :--- | :--- | :--- | :--- |
| **State Routing Engine** | Deterministic FSM | `app/agent.py` | 0% (Local Workstation) |
| **Layout Validator** | Automated Regex Scanning | `templates/` | 0% (Local Workstation) |
| **Generation Layer** | MCP Filesystem Context | Documentation & Commits | 0% (Local Workstation) |

---
## Project Directory Structure

```text
VibeShield-Compliance-Engine/
├── app/
│   ├── agent.py         # Primary State Graph Engine, Generation, & Repair Routines
│   └── validator.py     # Workspace Layout Scanner & Compliance Rules
├── templates/
│   ├── SKILL.md         # Reference Engineering Profile Specifications
│   └── STYLE_GUIDE.md   # Target Validation Layout Asset
└── tests/
    └── test_agent.py    # Verification Unit-Test Suite
```

## Local Execution Guide

Follow these steps to run and test the validation and automated healing framework on a local workstation.

1. Run the Verification Test Suite
Execute the automated unit tests to confirm proper component state transitions and edge routing logic:

    ```bash
        python -m unittest tests/test_agent.py
    ```

2. Run the Main Agent Framework
Execute the core engine to see the state graph process repository inputs, compile documentation changes, validate formatting, and display the execution path summary:

    ```bash
    python app/agent.py
    ```

3. Boundary Testing (Verifying the Self-Healing Loop)
To simulate a structural violation and observe the framework intercept and correct it automatically:

    1.Open templates/STYLE_GUIDE.md and append the invalid placeholder text [INSERT TEMPLATE HERE] to the bottom of the file.

    2.Save the file.

    3.Execute the agent engine in the terminal:

    ```bash
        python app/agent.py
    ```

Review the log output trace to verify that the pipeline intercepts the placeholder error, routes execution to the recovery routine, automatically removes the invalid string from the physical file on disk, and exits with a successful compliant status.

---

## Technical Status

This framework is maintained as an active, zero-overhead developer utility. The architecture is optimized strictly for local repository auditing, formatting verification, and automated workspace contextualization.

