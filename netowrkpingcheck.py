import subprocess
import platform
import time
import os
import ipaddress
import socket

hosts_input = input("DNS or IP: ")
hosts = hosts_input.split()

param = "-n" if platform.system().lower() == "windows" else "-c"
file_name = "hosts_status.txt"

if not os.path.exists(file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Host Status\n===========\n")

for host in hosts:
    result = subprocess.call(
        ["ping", param, "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    reachable = (result == 0)

    resolved_ip = None
    ip_type = None

    try:
        ip_obj = ipaddress.ip_address(host)
        resolved_ip = str(ip_obj)
    except ValueError:
        try:
            resolved_ip = socket.gethostbyname(host)
            ip_obj = ipaddress.ip_address(resolved_ip)
        except socket.gaierror:
            resolved_ip = "Unresolved"
            ip_obj = None

    if ip_obj:
        ip_type = "Private IP" if ip_obj.is_private else "Public IP"

    status = "ONLINE" if reachable else "OFFLINE"

    print(f"{host} ({ip_type} -> {resolved_ip}): {status}")

    with open(file_name, "a", encoding="utf-8") as f:
        f.write(f"{host} ({ip_type} -> {resolved_ip}): {status}\n")

    time.sleep(1)
