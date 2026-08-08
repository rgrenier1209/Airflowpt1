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


Setup & Installation
Clone the repository

Bash
git clone [https://github.com/rgrenier1209/Airflowpt1.git](https://github.com/rgrenier1209/Airflowpt1.git)
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

# Ticket Sales Data Pipeline

Python script to Extract, Transform, and load ticket sale data from a CSV into a MySQL database. Last it will print out the events that sold the most tickets.

## Getting Started

### Prerequisites

To run this project, you will need the following installed on your local environment:

* **Python 3.8+** (via Anaconda or standard Python installation)
* **MySQL Server & MySQL Workbench**
* **Git**

Required Python packages:
```bash
pip install pandas mysql-connector-python
```

### Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rgrenier1209/TicketSalePipeline.git
   cd TicketSalePipeline
   ```

2. **Prepare the Database & Table Schema**
   * The database table **must be premade** with the exact schema below prior to running the script.
   * The table **must be completely empty** (no existing records) to avoid primary key/duplicate entry conflicts.

   Run the following script in MySQL Workbench:
   ```sql
   CREATE DATABASE IF NOT EXISTS ticket_sales;
   USE ticket_sales;

   -- Create table with appropriate schema
   CREATE TABLE IF NOT EXISTS sales (
       ticket_id INT PRIMARY KEY,
       trans_date DATETIME,
       event_id INT,
       event_name VARCHAR(50),
       event_date DATE,
       event_type VARCHAR(10),
       event_city VARCHAR(20),
       customer_id INT,
       price DECIMAL(10,2),
       num_tickets INT
   );

   -- Ensure the table is empty before executing the pipeline
   TRUNCATE TABLE sales;
   ```

3. **Configure Connection & File Paths**
   * Open `TicketSalePipeline.py` and verify your MySQL credentials in `get_db_connection()`:
     ```python
     user='root'
     password='your_password'
     host='127.0.0.1'
     port='3306'
     database='ticket_sales'
     ```
   * Ensure the CSV path points to your local file location:
     ```python
     load_third_party(conn, r"C:\Path\To\Your\third_party_sales_1.csv")
     ```

4. **Run the Data Pipeline**
   Execute the main script from your terminal:
   ```bash
   python TicketSalePipeline.py
   ```

   **Expected Output:**
   ```text
   Successfully connected to the database!
   Here are the most popular tickets in the past month:
   - The North American International Auto Show
   - Carlisle Ford Nationals
   - Monster Jam
   ```

---

## Running the Tests

### Integration & Execution Tests
Verify that records are successfully ingested into MySQL:

1. Execute `python TicketSalePipeline.py`.
2. Query your MySQL console:
   ```sql
   SELECT COUNT(*) FROM ticket_sales.sales;
   ```
3. Confirm that the row count matches the number of rows in `third_party_sales_1.csv`.

---

## Built With

* [Python 3](https://www.python.org/) - Core programming language
* [pandas](https://pandas.pydata.org/) - Data ingestion and parsing
* [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/) - MySQL database interface
* [MySQL Workbench](https://www.mysql.com/products/workbench/) - Relational database management system

---

## Authors

* **Ricardo Grenier** - *Initial Work & Pipeline Construction* - [rgrenier1209](https://github.com/rgrenier1209)