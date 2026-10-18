

def detect_incidents(metrics):
    cpu = metrics["cpu_usage"]
    memory = metrics["memory_usage"]
    disk = metrics["disk_usage"]

    if cpu >= 95:
        cpu_status = "CRITICAL"
    elif cpu >=80.0:
        cpu_status = "WARNING"
    else:
        cpu_status = "NORMAL"

    if memory >= 95:
        memory_status = "CRITICAL"
    elif  memory >=80.0:
        memory_status = "WARNING"
    else:
        memory_status = "NORMAL"

    if disk >= 95:
        disk_status = "CRITICAL"

    elif disk >=80.0:
        disk_status = "WARNING"
    else:
        disk_status = "NORMAL"

    return {
        "cpu" : cpu_status,
        "memory" : memory_status,
        "disk" : disk_status
    }

testing = {
    "cpu_usage": 25,
    "memory_usage": 40,
    "disk_usage": 96
}
print(detect_incidents(testing))