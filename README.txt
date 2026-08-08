# Market Volatility Tracker Pipeline

Apache Airflow data pipeline designed to extract 1-minute interval stock market data for AAPL and TSLA, isolate date-stamped execution directories, move processed datasets, and execute downstream analytics.

## Getting Started

### Prerequisites

To run this project, you will need the following installed on your local environment:

* Docker & Docker Desktop (with Docker Compose)
* Python 3.10+
* Git

Required Python packages inside the Airflow environment:
pip install apache-airflow pandas yfinance

### Setup & Installation

1. Clone the repository
   git clone https://github.com/rgrenier1209/MarketVolatilityPipeline.git
   cd MarketVolatilityPipeline

2. Verify Project Structure
   Ensure your local directory contains the following layout:
   .
   ├── dags/
   │   └── marketvol_3.py
   ├── docker-compose.yaml
   └── README.md

3. Start the Airflow Stack in Docker
   Launch the containerized environment in detached mode:
   docker compose up -d

4. Enable the DAG in the Airflow UI
   * Navigate to http://localhost:8080 in your browser.
   * Locate the marketvol DAG and toggle the switch to ON (blue).
   * Optionally, click the Trigger DAG (Play) button to test an immediate manual execution.

   Expected Output Log (from t5 / run_market_query):
   === Market Analysis for YYYY-MM-DD ===
   AAPL Total Rows: 390
   TSLA Total Rows: 390

---

## Running the Tests

### Scheduler & Execution Verification

1. Check that all containers are active:
   docker compose ps

2. Export and review the Airflow scheduler logs to confirm successful task scheduling across execution runs:
   docker logs airflow-docker-airflow-scheduler-1 > scheduler.log

3. Inspect scheduler.log to confirm that tasks t0 through t5 execute sequentially according to defined dependencies without task failures.

---

## Built With

* Python 3 - Core programming language (https://www.python.org/)
* Apache Airflow - Workflow management and DAG orchestration (https://airflow.apache.org/)
* pandas - Data loading and dataset analysis (https://pandas.pydata.org/)
* yfinance - Financial market data extraction (https://pypi.org/project/yfinance/)
* Docker - Containerized deployment environment (https://www.docker.com/)

---

## Authors

* Ricardo Grenier - Initial Work & Pipeline Construction - https://github.com/rgrenier1209