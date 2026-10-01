#Anthony Rodriguez, Kumo-Ops 
import time
import json
import psutil 
import platform 
import socket 
from datetime import datetime

#python dictonary to get computing system metrics 
def get_system_metrics():
        
    hostname = socket.gethostname()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('C:\\').percent
    boot_time = psutil.boot_time()
    processcount = int(len(list(psutil.process_iter())))
    uptime = datetime.now() - datetime.fromtimestamp(boot_time)
    local_IP = socket.gethostbyname(hostname)
    byte_counter = psutil.net_io_counters()


    metrics = {
        "hostname": hostname,
        "os": f"{platform.system()} {platform.release()}",
        "time": datetime.now().strftime("%m-%d-%Y %H:%M:%S"), #format second !
        "cpu_usage": cpu,
        "memory_usage": memory,
        "disk_usage": disk,
        "process_count": processcount,
        "up_time": str(uptime),
        "local_IP": local_IP,
        "bytes_sent": byte_counter.bytes_sent,
        "bytes_recv": byte_counter.bytes_recv
    }
    return metrics

# Display the metrics in a readable format
def display_metrics(metrics):
    print(f"Hostname: {metrics['hostname']}")
    print(f"Operating System: {metrics['os']}")
    print(f"Current Time: {metrics['time']}")
    print(f"CPU Usage: {metrics['cpu_usage']}%")
    print(f"Memory Usage: {metrics['memory_usage']}%")
    print(f"Disk Usage: {metrics['disk_usage']}%")
    print(f"Process Count: {metrics['process_count']}")
    print(f"Uptime: {metrics['up_time']}")
    print(f"Local IP Address: {metrics['local_IP']}")
    print(f"Bytes Sent: {metrics['bytes_sent']}")
    print(f"Bytes Received: {metrics['bytes_recv']}")
    print("-" * 40)

#  Save metrics to a JSON log file 
def save_metrics(metrics):
    try:
        with open("metrics.json", "r") as metrics_file:
            data = json.load(metrics_file)
    except FileNotFoundError:
        data = []

    data.append(metrics)
    
    with open("metrics.json", "w") as metrics_file:
        json.dump(data, metrics_file)


while True:
    metrics = get_system_metrics()
    display_metrics(metrics)
    save_metrics(metrics)
    time.sleep(4)



