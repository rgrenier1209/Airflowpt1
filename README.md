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