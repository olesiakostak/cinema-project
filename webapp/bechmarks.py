import time
import concurrent.futures
from django.db import connection
import pandas as pd
import plotly.express as px

def run_query():
    from app.catalog.repositories import unit_of_work
    _ = list(unit_of_work.films.get_all().values('id'))
    connection.close()

def benchmark_execution(n_requests, max_workers, mode="thread"):
    start_time = time.time()

    if mode == "thread":
        Executor = concurrent.futures.ThreadPoolExecutor
    else:
        Executor = concurrent.futures.ProcessPoolExecutor

    with Executor(max_workers=max_workers) as executor:
        futures = [executor.submit(run_query) for _ in range(n_requests)]

        concurrent.futures.wait(futures)

    end_time = time.time()
    return end_time - start_time

def run_experiments(n_requests=100):
    worker_options = [1, 2, 4, 8]
    results = []

    for w in worker_options:
        time_thread = benchmark_execution(n_requests, w, "thread")
        results.append({"workers": w, "time": time_thread, "type": "Thread"})

    for w in worker_options:
        time_thread = benchmark_execution(n_requests, w, "process")
        results.append({"workers": w, "time": time_thread, "type": "Process"})

    return results

def get_benchmark_chart():
    results = run_experiments(n_requests=150) 
    
    df = pd.DataFrame(results)
    
    if not df.empty:
        fig = px.line(
            df, 
            x="workers", 
            y="time", 
            color="type", 
            title="Thread vs Process Benchmark",
            markers=True 
        )
        return fig.to_html(full_html=False)
    
    return "<p>Error</p>"

