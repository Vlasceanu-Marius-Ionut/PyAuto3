import subprocess
import platform
import time
import os

hosts_input = input("DNS or IP: ")
hosts = hosts_input.split()

param = "-n" if platform.system().lower() == "windows" else "-c"
file_name = "hosts_status.txt"

if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write("Host Status\n===========\n")

for host in hosts:
    result = subprocess.call(["ping", param, "1", host], stdout=subprocess.DEVNULL)
    reachable = (result == 0)

    if host.startswith(("192.", "10.", "172.")):
        ip_type = "Private IP"
    else:
        ip_type = "Public IP"

    status = "ONLINE" if reachable else "OFFLINE"
    print(f"{host} ({ip_type}): {status}")

    with open(file_name, "a") as f:
        f.write(f"{host} ({ip_type}): {status}\n")

    time.sleep(1)
