import pandas as pd
import yfinance as yf
import os
from datetime import datetime, timedelta, date
from airflow.decorators import dag, task
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator

default_args = {
    'owner': 'rick',
    'start_date': datetime(2026, 8, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

def download_stock_data(symbol, ds):
    start_date = date.today()
    end_date = start_date + timedelta(days=1)

    df = yf.download(symbol, start=start_date, end=end_date, interval='1m')

    output_dir = f"/tmp/data/{ds}"
    os.makedirs(output_dir, exist_ok = True)
    file_path = os.path.join(output_dir, f"{symbol}.csv")
    df.to_csv(file_path)

def analyze_market_data(ds):
    processed_dir = f"/tmp/processed_data/{ds}"
    aapl_path = os.path.join(processed_dir, "AAPL.csv")
    tsla_path = os.path.join(processed_dir, "TSLA.csv")

    aapl_df = pd.read_csv(aapl_path)
    tsla_df = pd.read_csv(tsla_path)

    # Custom query logic
    print(f"=== Market Analysis for {ds} ===")
    print(f"AAPL Total Rows: {len(aapl_df)}")
    print(f"TSLA Total Rows: {len(tsla_df)}")


@dag(
    dag_id='marketvol',
    default_args=default_args,
    description='mkt vol tracker',
    schedule= '0 18 * * 1-5', #Runs @6pm weekdays,
    catchup=False
)

def marketvol_pipeline():
    t0 = BashOperator(
        task_id='create_temp_dir',
        bash_command='mkdir -p /tmp/data/{{ ds }}'
    )
    t1 = PythonOperator(
        task_id = 'download_aapl_data',
        python_callable = download_stock_data,
        op_kwargs={
            'symbol': 'AAPL',
            'ds': '{{ ds }}'
        }
    )
    t2 = PythonOperator(
        task_id = 'download_tsla_data',
        python_callable = download_stock_data,
        op_kwargs={
            'symbol': 'TSLA',
            'ds': '{{ ds }}'
        }
    )
    t3 = BashOperator(
        task_id = 'move_aapl_data',
        bash_command="""
            mkdir -p /tmp/processed_data/{{ ds }} && \
            mv /tmp/data/{{ ds }}/AAPL.csv /tmp/processed_data/{{ ds }}/AAPL.csv
        """    )
    t4 = BashOperator(
        task_id = 'move_tsla_data',
        bash_command="""
            mkdir -p /tmp/processed_data/{{ ds }} && \
            mv /tmp/data/{{ ds }}/TSLA.csv /tmp/processed_data/{{ ds }}/TSLA.csv
        """    )
    t5 = PythonOperator(
        task_id='run_market_query',
        python_callable=analyze_market_data,
        op_kwargs={
            'ds': '{{ ds }}'
        }
    )
    #Task dependencies
    t0 >> [t1, t2]
    t1 >> t3
    t2 >> t4
    [t3, t4] >> t5
# Instantiate the pipeline
marketvol_pipeline()