import json
import socket
import requests
import psutil

def ping_server(ip, port):
    try:
        sock = socket.create_connection((ip, port), timeout=3)
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False

def check_database_connection(host, port):
    try:
        sock = socket.create_connection((host, port), timeout=3)
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False

def check_api_endpoint(url):
    try:
        response = requests.get(url, timeout=3)
        return response.status_code == 200
    except requests.RequestException:
        return False

def check_system_health(cpu_threshold, memory_threshold):
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    return cpu_usage < cpu_threshold, memory_usage < memory_threshold

def load_config():
    with open("config.json") as config_file:
        return json.load(config_file)

def main():
    config = load_config()
    report_data = {"servers": [], "databases": [], "endpoints": [], "system_health": {}}

    for server in config["servers"]:
        status = ping_server(server["ip"], server["port"])
        report_data["servers"].append({"name": server["name"], "ip": server["ip"], "status": status})

    for db in config["databases"]:
        status = check_database_connection(db["host"], db["port"])
        report_data["databases"].append({"name": db["name"], "status": status})

    for endpoint in config["endpoints"]:
        status = check_api_endpoint(endpoint["url"])
        report_data["endpoints"].append({"name": endpoint["name"], "status": status})

    cpu_status, memory_status = check_system_health(config["cpu_threshold"], config["memory_threshold"])
    report_data["system_health"]["cpu_status"] = cpu_status
    report_data["system_health"]["memory_status"] = memory_status

    print("Health Check Completed. Report data:", report_data)
    return report_data

if __name__ == "__main__":
    main()

