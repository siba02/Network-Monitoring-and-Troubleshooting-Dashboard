import time
import json
import psutil
import subprocess

def get_netstats():
    result = subprocess.getoutput("ss -tuna")
    return result

def get_bandwidth():
    net = psutil.net_io_counters()
    return {
        "bytes_sent": net.bytes_sent,
        "bytes_recv": net.bytes_recv,
        "packets_sent": net.packets_sent,
        "packets_recv": net.packets_recv
    }

def get_system_load():
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent
    }

while True:
    metrics = {
        "timestamp": time.time(),
        "bandwidth": get_bandwidth(),
        "system_load": get_system_load(),
        "connections": get_netstats()
    }

    print(json.dumps(metrics), flush=True)
    time.sleep(5)
