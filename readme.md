# 🐍 SnakePlane

**SnakePlane** is a next-generation Python execution engine that turns ordinary Python scripts into distributed data pipelines — without requiring any special code from the developer. It analyzes your script's structure, builds a dataflow DAG behind the scenes, and dispatches scalable workloads to backends like Ray or Kubernetes.

> **Mission**: Make distributed execution feel native to Python users — fast, automatic, and elegant.

---

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run a Sample Script
```bash
python -m cli.main examples/simple_etl.py --dry-run
```

## 🔍 How It Works

- Parses Python script via AST
- Detects DataFrame-heavy operations
- Builds a runtime task graph (DAG)
- Schedules tasks using Ray (MVP)
- Supports compression for intermediate outputs

For a full architecture overview, see [docs/mvp_architecture.md](docs/mvp_architecture.md).

## 📁 Folder Structure

```
snakeplane/
├── engine/          # AST parsing + DAG creation
├── core/            # Backends and scheduler interface
├── compression/     # In-memory compression (Arrow + LZ4)
├── cli/             # CLI entrypoint
├── examples/        # Sample scripts
├── docs/            # Documentation
├── tests/           # Tests
└── snakeplane-plan.json
```

## 🛣️ Roadmap

- ✅ AST-based DAG planner
- ✅ Dry-run task scheduler (Ray)
- 🔄 Ray → Modin/Polars integration
- 🔄 Kubernetes-native autoscaling
- 🔄 Visual DAG explorer (CLI/web)
- 🔄 AI-powered self-optimization for task scheduling

## 🤝 Contributing

Contributions welcome — just fork and PR!

### Branch Naming Convention
```
feature/yourname/issue-123-short-description
```

## 📜 License

MIT License