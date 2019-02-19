from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator


dag = DAG('hello_friends',
          description='Hello Friends DAG',
          schedule_interval='0 17 * * *',
          start_date=datetime(2019, 2, 10)
          )


dummy_task = DummyOperator(task_id='dummy_task_id',
                           retries=5,
                           dag=dag)


def print_hello():
    return 'Hello world :)'

python_task = PythonOperator(task_id='python_task_id',
                             python_callable=print_hello,
                             dag=dag)


my_friends = ["Anne", "Ted", "Bob", "Sue"]

templated_cmd = """
                {% for friend in params.friends %}
                    echo Hello {{friend}}!
                {% endfor %}
                """

bash_task = BashOperator(task_id='bash_task_id',
                         bash_command=templated_cmd,
                         params={"friends": my_friends},
                         dag=dag)


dummy_task >> python_task >> bash_task
