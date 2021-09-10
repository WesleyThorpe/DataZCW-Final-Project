import sqlite3
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'email': ['wesley.thorpe@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'SCHEDULE',
    default_args=default_args,
    start_date=days_ago(2),
    description='Recommendations',
    schedule_interval='@daily',
    catchup=False)


def connect_in_query():
    conn = sqlite3.connect("./mlb.py")
    cur = conn.cursor()
    cur.execute("select * from MLB_DataFrame 5;")



def write_to_file():
    results = cur.fetchall()
    f = open("baseball.txt", "w")
    f.write(results)
    f.close
    #cur.description

def connect_in_query2():
    conn = sqlite3.connect("./nba.py")
    cur = conn.cursor()
    cur.execute("select;")

def write_to_file2():
    results = cur.fetchall()
    f = open("basketball.txt", "w")
    f.write(results)
    f.close
    #cur.description

def connect_in_query3():
    conn = sqlite3.connect("./nhl.py")
    cur = conn.cursor()
    cur.execute("select;")

def write_to_file3():
    results = cur.fetchall()
    f = open("hockey.txt", "w")
    f.write(results)
    f.close
    #cur.description
def connect_in_query4():
    conn = sqlite3.connect("./nfl.py")
    cur = conn.cursor()
    cur.execute("select;")

def write_to_file4():
    results = cur.fetchall()
    f = open("football.txt", "w")
    f.write(results)
    f.close
    #cur.description
def connect_in_query5():
    conn = sqlite3.connect("./movies.db")
    cur = conn.cursor()
    cur.execute("select;")

def write_to_file5():
    results = cur.fetchall()
    f = open("soccer.txt", "w")
    f.write(results)
    f.close
    #cur.description


connect_in_query = PythonOperator(task_id='connect_in_query',
    python_callable=connect_in_query)

write_to_file = PythonOperator(task_id='write_to_file',
    python_callable=write_to_file)

write_to_file2 = PythonOperator(task_id='write_to_file2',
    python_callable=write_to_file2)

write_to_file3 = PythonOperator(task_id='write_to_file3',
    python_callable=write_to_file3)

write_to_file4 = PythonOperator(task_id='write_to_file4',
    python_callable=write_to_file4)

write_to_file5 = PythonOperator(task_id='write_to_file5',
    python_callable=write_to_file5)

dag.add_task(connect_in_query)
dag.add_task(write_to_file)
dag.add_task(write_to_file2)
dag.add_task(write_to_file3)
dag.add_task(write_to_file4)
dag.add_task(write_to_file5)
    


connect_in_query>>write_to_file>>write_to_file2>>write_to_file3>>write_to_file4>>write_to_file5