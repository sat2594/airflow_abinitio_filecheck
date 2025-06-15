# Airflow DAG: File Check + Ab Initio Graph

This repository contains an Airflow DAG that:
- Checks if a specific file exists in a directory.
- If the file exists, it triggers an Ab Initio graph.

## Schedule
Runs every hour via Airflow.

## Folder Structure
- `dags/`: Contains the DAG definition.
- `scripts/`: Contains a shell script that runs the Ab Initio graph.

## Setup Instructions
1. Place the DAG in your Airflow DAGs folder.
2. Ensure `run_abinitio_graph.sh` points to the actual path to your graph and Ab Initio environment.
3. Update file path checks as needed.
