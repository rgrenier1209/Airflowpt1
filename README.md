# Market Volatility Tracker Pipeline

Apache Airflow data pipeline designed to extract 1-minute interval stock market data for AAPL and TSLA, isolate date-stamped execution directories, move processed datasets, and execute downstream analytics.

## Getting Started

### Prerequisites

To run this project, you will need the following installed on your local environment:

* **Docker & Docker Desktop** (with Docker Compose)
* **Python 3.10+**
* **Git**

Required Python packages inside the Airflow environment:
```bash
pip install apache-airflow pandas yfinance
```

### Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rgrenier1209/Airflowpt1.git
   cd Airflowpt1
   ```

2. **Verify Project Structure**
   Ensure your local directory contains the following layout:
   ```text
   .
   ├── dags/
   │   └── marketvol_3.py
   ├── docker-compose.yaml
   └── README.md
   ```

3. **Start the Airflow Stack in Docker**
   Launch the containerized environment in detached mode:
   ```bash
   docker compose up -d
   ```

4. **Enable the DAG in the Airflow UI**
   * Navigate to `http://localhost:8080` in your browser.
   * Locate the **`marketvol`** DAG and toggle the switch to **ON** (blue).
   * Optionally, click the **Trigger DAG** (Play) button to test an immediate manual execution.

   **Expected Output Log (from `t5` / `run_market_query`):**
   ```text
   === Market Analysis for YYYY-MM-DD ===
   AAPL Total Rows: 390
   TSLA Total Rows: 390
   ```

---

## Running the Tests

### Scheduler & Execution Verification

1. **Check Container Status**
   Verify that all service containers are active:
   ```bash
   docker compose ps
   ```

2. **Export Scheduler Logs**
   Extract the execution log from the Airflow scheduler container to verify task scheduling across runs:
   ```bash
   docker logs airflow-docker-airflow-scheduler-1 > scheduler.log
   ```

3. **Inspect Output**
   Review `scheduler.log` to confirm that tasks `t0` through `t5` execute sequentially according to defined dependencies without task failures.

---

## Built With

* [Python 3](https://www.python.org/) - Core programming language
* [Apache Airflow](https://airflow.apache.org/) - Workflow management and DAG orchestration
* [pandas](https://pandas.pydata.org/) - Data loading and dataset analysis
* [yfinance](https://pypi.org/project/yfinance/) - Financial market data extraction
* [Docker](https://www.docker.com/) - Containerized deployment environment

---

## Authors

* **Ricardo Grenier** - *Initial Work & Pipeline Construction* - [rgrenier1209](https://github.com/rgrenier1209)
README.md
Displaying README.md.