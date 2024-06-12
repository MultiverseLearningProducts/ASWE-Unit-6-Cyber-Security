
import requests

def check_port_open(target_ip, port):
    url = f"http://{target_ip}:{port}"
    try:
        response = requests.get(url, timeout=1)
        print(f"Response status code for {url}: {response.status_code}")
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")
        return False

def check_sql_injection(url, param):
    print(f"Checking for SQL injection vulnerability at {url}")
    payload = "' OR '1'='1"
    response = requests.get(url, params={param: payload})
    
    if response.status_code == 200 and "Actors:" in response.text:
        print(f"SQL Injection vulnerability found with payload: {payload}")
        return True
    else:
        print("No SQL Injection vulnerability found.")
        return False

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    
    common_ports = [8080]  # Update to the port used by the Flask application

    open_ports = []
    for port in common_ports:
        if check_port_open(target_ip, port):
            open_ports.append(port)
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")

    print(f"Open ports on {target_ip}: {open_ports}")

    if 8080 in open_ports:
        url = f"http://{target_ip}:8080/actors"
        param = 'name'
        check_sql_injection(url, param)
