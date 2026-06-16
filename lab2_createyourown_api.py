from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/system-info")
def system_info():

    hostname = os.popen("hostname").read().strip()
    kernel = os.popen("uname -r").read().strip()
    systemuptime = os.popen("uptime").read().strip()
    cpuinformation = os.popen("lscpu").read().strip()
    memoryusage = os.popen("free -m").read().strip()


    return {
        "hostname": hostname,
        "kernel": kernel,
        "system uptime": systemuptime,
        "cpuinformation": cpuinformation,
        "memoryusage": memoryusage
    }
