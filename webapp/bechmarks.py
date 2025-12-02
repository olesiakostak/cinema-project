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



def run_experiment_with_workers(n_requests=50):
    worker_options = [1, 2, 4, 8]
    results = []

    for w in worker_options:
        time_thread = benchmark_execution(n_requests, w, "thread")
        results.append({"workers": w, "time": time_thread, "type": "Thread"})

    for w in worker_options:
        time_thread = benchmark_execution(n_requests, w, "process")
        results.append({"workers": w, "time": time_thread, "type": "Process"})

    return results


def run_experiment_with_requests(workers=4):
    request_counts = [10, 50, 100, 200, 400]

    results = []

    for n in request_counts:
        time_thread = benchmark_execution(n, workers, "thread")
        results.append({"requests": n, "time": time_thread, "type": "Thread"})
 
        time_proc = benchmark_execution(n, workers, "process")
        results.append({"requests": n, "time": time_proc, "type": "Process"})
        
    return results

def get_benchmark_chart():
    res_work = run_experiment_with_workers() 
    df_work = pd.DataFrame(res_work)
    
    html_work = "<p>Error in Worker Benchmark</p>"
    if not df_work.empty:  
        fig1 = px.line(
            df_work, 
            x="workers", 
            y="time", 
            color="type", 
            title="Dependence on Workers Count (Threads vs Processes)",
            markers=True 
        )
        html_work = fig1.to_html(full_html=False)
    
   
    res_req = run_experiment_with_requests()
    df_req = pd.DataFrame(res_req)
    
    html_req = "<p>Error in Request Benchmark</p>"
    if not df_req.empty:
        fig2 = px.line(
            df_req,
            x="requests",
            y="time",
            color="type",
            title="Dependence on Requests Count",
            markers=True
        )
        html_req = fig2.to_html(full_html=False)

    return html_work, html_req


