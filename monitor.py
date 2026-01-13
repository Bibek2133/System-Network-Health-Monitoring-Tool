import psutil
import platform
import subprocess
import socket
from datetime import datetime

#OS Information
def get_os_info():
    return platform.system(), platform.release()

# CPU Information
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Memory Information
def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

# Disk Information
def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

# Ping test
def ping_test(host="8.8.8.8"):
    try:
        subprocess.check_output(
            ["ping", "-n", "2", host],
            stderr=subprocess.STDOUT
        )
        return "OK"
    except:
        return "FAILED"

# DNS Resolution Test
def dns_test():
    try:
        socket.gethostbyname("www.google.com")
        return "OK"
    except:
        return "FAILED"

# Status Classification
def classify_status(value, warning, critical):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    else:
        return "OK"

#Logging Results
def log_result(message):
    with open("system_health.log", "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

#Generate Support Report
def generate_report(data):
    with open("report.txt", "w") as report:
        report.write("SYSTEM & NETWORK HEALTH REPORT\n")
        report.write("="*40 + "\n\n")
        for key, value in data.items():
            report.write(f"{key}: {value}\n")

def main():
    os_name, os_version = get_os_info()
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    cpu_status = classify_status(cpu, 70, 85)
    mem_status = classify_status(memory, 75, 90)
    disk_status = classify_status(disk, 70, 85)

    ping = ping_test()
    dns = dns_test()

    results = {
        "OS": f"{os_name} {os_version}",
        "CPU Usage": f"{cpu}% ({cpu_status})",
        "Memory Usage": f"{memory}% ({mem_status})",
        "Disk Usage": f"{disk}% ({disk_status})",
        "Ping Test": ping,
        "DNS Test": dns
    }

    for k, v in results.items():
        log_result(f"{k} - {v}")

    generate_report(results)
    print("Health check completed. Report generated.")

if __name__ == "__main__":
    main()
