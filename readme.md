🐍 SnakePlane
SnakePlane is a Python-native distributed execution layer that turns ordinary Python scripts into scalable workloads without requiring developers to rewrite their code.

It analyzes Python code, detects expensive data and compute patterns, builds an execution DAG, and routes work through scalable backends such as Ray, Docker, Kubernetes, and future dataframe/runtime engines.

Mission: Make distributed execution feel native to Python users — no rewrites, no setup hell, no infrastructure ceremony.

Planning Links
Roadmap / Notion: https://www.notion.so/NEUROSPECT-221126fae7f480eab2baed5857405d93
Linear: Not linked yet
No Linear URL or Linear-style issue key was found in the exported Notion docs.

If a Linear project or issue URL is added later, link it here:

Linear: https://linear.app/<workspace>/project/<project-id>
What SnakePlane Does
SnakePlane lets developers run familiar Python, pandas, NumPy, and data-processing scripts through an intelligent execution plane.

Instead of forcing users to rewrite code for Spark, Dask, Ray, or Kubernetes, SnakePlane aims to:

Parse ordinary Python scripts.
Detect dataframe-heavy and compute-heavy operations.
Build a task graph automatically.
Select an execution backend.
Optimize memory and intermediate data movement.
Run locally, in containers, or on cluster infrastructure.
Provide clear logs, plans, profiling, and DAG visibility.
Core Philosophy
SnakePlane is not a traditional operating system. It is a lightweight runtime plane for Python workloads.

Where a normal OS schedules a Python process on one machine, SnakePlane sits above the Python runtime and decides how the work should be split, optimized, routed, compressed, and executed.

The long-term goal is a Python execution layer that behaves like an autopilot:

No code changes for the user.
Automatic scaling across local cores, containers, or clusters.
Transparent acceleration through Modin, Polars, Arrow, Ray, and future runtimes.
Observable execution through plans, logs, profiling, metrics, and DAG views.
Future live optimization based on runtime behavior.
Quick Start
1. Install dependencies
pip install -r requirements.txt
2. Run a sample script
python -m cli.main examples/simple_etl.py --dry-run
or, once packaged as a CLI:

snakeplane run examples/simple_etl.py --dry-run
3. Expected execution flow
Python script
  → AST parser
  → workload detector
  → task graph builder
  → scheduler backend
  → execution/logging output
MVP Architecture
The MVP is focused on proving the end-to-end execution path:

User runs CLI
  → Script parsed with AST
  → Workload components identified
  → TaskGraph built
  → Tasks scheduled through Ray or dry-run backend
  → Compression simulated for intermediate frames
  → DAG/log output generated
Main Components
Component	Purpose
CLI Layer	Runs scripts, accepts flags, and prints execution output.
Engine Layer	Parses Python AST and detects expensive operations.
Task Graph	Represents detected work as DAG nodes and edges.
Scheduler Layer	Dispatches or simulates tasks through selected backend.
Smart Data Layer	Routes dataframe work through pandas-compatible acceleration paths.
Compression Layer	Handles Arrow/LZ4/BLOSC-style intermediate frame storage.
Observability Layer	Emits logs, execution plans, profiling data, and future DAG views.
Repository Structure
snakeplane/
├── cli/             # CLI entrypoints and command handling
├── core/            # Backends, scheduler interface, runtime orchestration
├── engine/          # AST parsing, workload detection, and DAG creation
├── compression/     # In-memory compression and frame IO
├── data/            # Future smart dataframe/data layer
├── infra/           # Future Docker/Kubernetes/cloud runtime adapters
├── examples/        # Sample scripts
├── docs/            # Architecture and roadmap documentation
├── tests/           # Unit and integration tests
└── snakeplane-plan.json
Roadmap Phases
Phase 0 — Foundation & Project Setup
Goal: Establish the repository, architecture, tooling, and MVP scope.

Included work:

Initialize GitHub repository.
Create initial folder structure.
Define MVP architecture.
Decide MVP scheduler direction.
Decide compression format direction.
Create documentation skeleton.
Freeze MVP scope.
Add GitHub issue automation.
Current status: Mostly complete.

Completed foundation items include repo setup, scheduler/compression decisions, MVP scope documentation, system architecture, project docs skeleton, config schema, config loader, and GitHub issue automation.

Phase 1 — MVP Execution Engine
Goal: Allow a user to run a normal Python script and generate a scalable execution plan.

Included work:

Define MVP configuration schema.
Implement config loader.
Build CLI entrypoint.
Write script runner.
Parse Python scripts with AST.
Walk AST nodes and detect relevant structure.
Detect dispatchable patterns such as loops, apply, groupby, dataframe loads, and file IO.
Label AST nodes with metadata such as line number, operation type, and estimated workload size.
Build TaskNode and TaskGraph classes.
Log simulated dispatch flow.
Generate snakeplane-plan.json.
Add text-mode DAG visualization.
Create examples/simple_etl.py.
Add parser and compression tests.
Document MVP architecture and CLI usage.
Validate an end-to-end dry run.
Expected outcome:

A developer can run:

python -m cli.main examples/simple_etl.py --dry-run
and see a planned execution graph without changing the original script.

Current task status from Notion export:

Status	Items
Done	Repo initialization, config schema, config loader, architecture docs, MVP scope, tooling decisions, GitHub issue automation
In progress	CLI entrypoint
Not started	Runner, AST walker, dispatch pattern detection, task graph, scheduler interface, Ray mock backend, compression wrapper, JSON DAG output, visualizer, example script, tests, docs
Phase 2 — Ray Runtime & Scheduler Backend
Goal: Move from dry-run planning to real distributed task execution.

Included work:

Design the SchedulerBackend interface.
Implement Ray backend support.
Add backend selector in config and CLI.
Map task graph nodes to scheduler tasks.
Support local multicore execution.
Improve task-level logs.
Add failure handling and backend fallback behavior.
Expected outcome:

SnakePlane can run simple Python/dataframe workloads through Ray while preserving the same user-facing script flow.

Notes:

The scheduler evaluation compared Ray, Dask, and Fugue. Ray is the practical MVP choice because it integrates tightly with Python-native scheduling and Modin, while Fugue remains a possible future abstraction for higher-level workflows.

Phase 3 — Smart DataFrame Engine
Goal: Add transparent dataframe acceleration.

Included work:

Add pandas-compatible dataframe routing.
Evaluate Modin with Ray backend.
Evaluate Polars for high-performance dataframe operations.
Support CSV and Parquet inputs.
Add Arrow-backed memory layout where useful.
Route selected pandas-style operations to faster distributed dataframe engines.
Benchmark pandas vs Modin vs Polars paths.
Expected outcome:

SnakePlane can accelerate dataframe-heavy scripts without requiring users to manually rewrite pandas code.

Phase 4 — Compression & Intermediate Storage
Goal: Improve memory efficiency and data movement between tasks.

Included work:

Enable compression format toggle.
Implement store_frame() and load_frame() helpers.
Support Arrow + LZ4/BLOSC-style frame storage.
Evaluate Zstd for high-ratio batch jobs.
Simulate local disk, tmpfs, or future object-storage-backed intermediate storage.
Log compression/decompression timing.
Expected outcome:

Intermediate dataframe outputs can be stored, compressed, reloaded, and measured as part of the execution flow.

Default strategy:

Default: Apache Arrow + BLOSC + LZ4
High-ratio option: Apache Arrow + BLOSC + Zstd
Fallback: no compression or raw LZ4 for special cases
Phase 5 — Docker Runtime & Local Orchestration
Goal: Make SnakePlane portable across local and containerized environments.

Included work:

Add Docker runtime adapter.
Package runtime dependencies into a Docker image.
Support local vs Docker execution modes.
Add CLI/config flags for execution mode.
Prepare container structure for future Kubernetes support.
Improve environment consistency across developer machines.
Expected outcome:

Users can run the same SnakePlane workflow locally or inside Docker with minimal setup differences.

Phase 6 — Kubernetes & Cloud Scaling
Goal: Expand SnakePlane from local/container execution to cluster-backed execution.

Included work:

Add Kubernetes-native execution support.
Explore Ray-on-Kubernetes deployment patterns.
Add autoscaling configuration.
Add cloud runner hooks such as ECS or similar container orchestration targets.
Define local, Docker, cluster, and cloud execution profiles.
Improve remote intermediate storage strategy.
Expected outcome:

SnakePlane can move from laptop execution to infrastructure-backed execution without changing user scripts.

Phase 7 — Observability, Debugging & DAG Visualization
Goal: Make SnakePlane easier to inspect, trust, and debug.

Included work:

Add richer CLI logging.
Add local profiling with CPU and memory visibility.
Add task-level timing.
Add DAG JSON output.
Add text-mode DAG visualizer.
Explore lightweight web or notebook DAG visualization.
Add monitoring/debug panel for MVP workflows.
Expected outcome:

Developers can understand what SnakePlane detected, why it scheduled work a certain way, and where bottlenecks appear.

Phase 8 — Auto-Optimizer
Goal: Turn SnakePlane into a performance-aware runtime that can improve execution choices.

Included work:

Collect runtime traces.
Detect CPU-bound, IO-bound, and memory-bound operations.
Recommend backend choices.
Recommend partitioning strategies.
Add config-driven optimization controls.
Explore speculative execution and adaptive batching.
Prepare for live optimization and feedback loops.
Expected outcome:

SnakePlane can make smarter scheduling and optimization decisions based on workload shape and observed runtime behavior.

Phase 9 — Live Optimization Layer
Goal: Add dynamic runtime intelligence that can adapt execution while code runs.

Included work:

Monitor Python execution in real time.
Detect bottlenecks and scaling opportunities.
Route operations to better backends dynamically.
Switch between pandas, Modin, Polars, Arrow, and compiled paths where appropriate.
Track workload history across runs.
Use feedback to improve future execution plans.
Expected outcome:

SnakePlane behaves like an autopilot for Python performance: observing, rerouting, optimizing, and learning without requiring user changes.

Phase 10 — Public Release & Ecosystem
Goal: Package SnakePlane into a stable, documented, public developer tool.

Included work:

Package for installation.
Expand user guide and developer docs.
Add benchmark results.
Add examples and tutorials.
Add contributing guide.
Finalize release roadmap.
Prepare public launch materials.
Add cloud hooks where stable.
Expected outcome:

SnakePlane reaches a stable public release with docs, examples, benchmarks, and a clear contribution path.

Release Milestones
Version	Focus
v0.1	Local script scaling
v0.2	Docker + CLI integration
v0.3	Kubernetes support
v0.5	Auto-optimizer with config file
v1.0	Stable public release with docs and cloud hook
MVP Success Criteria
The MVP is successful when:

A user can install SnakePlane and run a normal Python script.
The script can be analyzed without user code changes.
Dataframe and compute-heavy operations are detected.
A DAG can be generated and printed.
A scheduler backend can simulate or execute the plan.
Intermediate frame compression can be toggled.
CSV and Parquet inputs are supported.
Basic logs, profiling, and debug output are available.
The workflow is documented with examples.
MVP Tech Stack
Area	Tech
Distributed Compute	Ray, with multiprocessing fallback
DataFrames	Modin, optional Polars path, pandas-compatible routing
Format & Compression	Apache Arrow, LZ4, BLOSC, optional Zstd
Task Scheduling	Ray or custom micro-scheduler
Containerization	Docker, Kubernetes-ready build
CLI & Config	Click, YAML, psutil, rich
Logging	loguru, rich console, future web logs
Not in the MVP
These are roadmap items, not initial MVP requirements:

Full Kubernetes deployment manager.
Real-time Kubernetes autoscaling.
PyPy, Numba, or JIT-level optimization.
User-facing extensibility SDK.
Workflow DAG orchestration UI.
Notebook or GUI interface.
Multi-user support or authentication.
SQL or streaming source support.
Example Output
Detected DataFrame load at line 5
Detected apply() inside for loop at line 14
Planned DAG:
    LoadCSV → Clean → Apply → GroupBy → Export
Backend: Ray
Dry Run: Enabled
Documentation
MVP Architecture
Notion export includes user docs, project docs, benchmark planning, release strategy, setup notes, and technology evaluations.
Contributing
Contributions are welcome.

Branch Naming Convention
feature/yourname/issue-123-short-description
bugfix/yourname/issue-123-short-description
hotfix/yourname/issue-123-short-description
License
MIT License
