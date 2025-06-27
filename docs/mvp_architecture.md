# 🧠 SnakePlane – MVP Architecture

## 📐 Overview

**SnakePlane** is a next-generation, performance-aware, distributed Python execution engine that allows you to run ordinary `pandas`-based scripts across containerized environments (Ray, Docker, Kubernetes) **without rewriting your code**.

The MVP is focused on:
- Parsing Python scripts
- Identifying heavy operations
- Building a task DAG
- Dispatching tasks using Ray
- Simulating compression and intermediate storage

---

## 🧱 Architecture Components

### 1. CLI Layer (`cli/main.py`)
- Entrypoint to run Python scripts (`snakeplane-run script.py`)
- Parses arguments like `--dry-run`, `--backend=ray`
- Outputs DAG summary and scheduling decisions

### 2. Engine Layer (`engine/`)
- Uses Python's `ast` module to parse scripts
- Detects:
  - DataFrame loads
  - Loops
  - CPU-heavy ops (e.g., `apply`, `groupby`)
- Builds a `TaskGraph` DAG with metadata about each node

### 3. Scheduling Layer (`core/backends/`)
- Interfaces with backend like Ray
- Runs simulated or real parallel tasks
- Supports dry-run mode for development/testing

### 4. Compression Layer (`compression/io.py`)
- (Mocked) Arrow + LZ4 compression for in-memory dataframes
- Simulates intermediate storage on local disk, S3, or tmpfs
- Measures compression and decompression time

### 5. DAG Output Layer
- Saves execution plan to a `.json` file
- Pretty-prints a text-based view of the execution graph
- Sets the foundation for future visualization tools

---

## 🔄 Execution Flow (MVP)

```text
User runs CLI →
    Script parsed with AST →
        Workload components identified →
            TaskGraph built →
                Tasks scheduled (Ray) →
                    Compression applied (mocked) →
                        Output logged, DAG printed
```

## 🧪 Example Use Case

**Command:**
```bash
snakeplane-run examples/simple_etl.py --dry-run
```

**Output:**
```plaintext
Detected DataFrame load at line 5
Detected apply() inside for loop at line 14
Planned DAG:
    LoadCSV → Clean → Apply → GroupBy → Export
Backend: Ray
Dry Run: Enabled
```

## 🔧 Tools and Technologies

- **Python AST** – Script introspection and static analysis
- **Ray** – Distributed execution backend
- **Apache Arrow** – Columnar memory layout
- **LZ4** – Fast compression for intermediate frames
- **Graphviz / Text view** – DAG visualization (optional CLI mode)

## 📁 MVP Project Layout

```
snakeplane/
├── engine/          # AST parsing + DAG creation
├── core/            # Backend scheduling
├── compression/     # Frame compression utilities
├── cli/             # CLI tool
├── examples/        # User-facing scripts
├── docs/            # Architecture, roadmap
├── tests/           # Unit + integration tests
├── requirements.txt
├── pyproject.toml
└── snakeplane-plan.json
```

## 🧭 Post-MVP Roadmap

- Add support for Modin and Polars as pluggable execution engines
- Enable native Kubernetes and ECS orchestration with autoscaling
- Build an interactive DAG web visualizer
- Implement speculative execution and performance profiling
- Introduce AI-powered runtime self-optimization:
  - Analyze past execution traces
  - Optimize future task scheduling and memory allocation automatically
- Add SQL interface layer (e.g., Fugue-style transformations)

## 🧵 Summary

SnakePlane's MVP delivers a developer-first experience for distributed computation — parsing Python scripts and transforming them into scalable DAGs. The system is lightweight, introspective, and modular — laying a powerful foundation for future AI-assisted execution and smart orchestration.