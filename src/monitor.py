#Anthony Rodriguez, Kumo-Ops 
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


result = get_system_metrics()
print(result)
