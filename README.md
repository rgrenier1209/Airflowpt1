Market Volatility Tracker Pipeline
Apache Airflow data pipeline designed to extract 1-minute interval stock market data for AAPL and TSLA, isolate date-stamped execution directories, move processed datasets, and execute downstream analytics.

Getting Started
Prerequisites
To run this project, you will need the following installed on your local environment:

Docker & Docker Desktop (with Docker Compose)

Python 3.10+

Git

Required Python packages inside the Airflow environment:

Bash
pip install apache-airflow pandas yfinance
Setup & Installation
Clone the repository

Bash
git clone https://github.com/rgrenier1209/Airflowpt1.git
cd Airflowpt1
Verify Project Structure
Ensure your local directory contains the following layout:

Plaintext
.
├── dags/
│   └── marketvol_3.py
├── docker-compose.yaml
└── README.md
Start the Airflow Stack in Docker
Launch the containerized environment in detached mode:

Bash
docker compose up -d
Enable the DAG in the Airflow UI

Navigate to http://localhost:8080 in your browser.

Locate the marketvol DAG and toggle the switch to ON (blue).

Optionally, click the Trigger DAG (Play) button to test an immediate manual execution.

Expected Output Log (from t5 / run_market_query):

Plaintext
=== Market Analysis for YYYY-MM-DD ===
AAPL Total Rows: 390
TSLA Total Rows: 390
Running the Tests
Scheduler & Execution Verification
Check Container Status
Verify that all service containers are active:

Bash
docker compose ps
Export Scheduler Logs
Extract the execution log from the Airflow scheduler container to verify task scheduling across runs:

Bash
docker logs airflow-docker-airflow-scheduler-1 > scheduler.log
Inspect Output
Review scheduler.log to confirm that tasks t0 through t5 execute sequentially according to defined dependencies without task failures.

Built With
Python 3 - Core programming language

Apache Airflow - Workflow management and DAG orchestration

pandas - Data loading and dataset analysis

yfinance - Financial market data extraction

Docker - Containerized deployment environment

Authors
Ricardo Grenier - Initial Work & Pipeline Construction - rgrenier1209