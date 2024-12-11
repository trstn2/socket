import socket
import threading


def scan_port(ip, port, port_status):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((ip, port))
            port_status.append((port, "Open"))
            print(f"Port {port} is open.")
        except (socket.timeout, ConnectionRefusedError):
            port_status.append((port, "Closed"))
        except socket.error as err:
            print(f"Error scanning port {port}: {err}")


def scan_ports(start_port, ip="YOUR_IP_HERE"):
    port_status = []
    threads = []

    for port in range(start_port, 65536):
        thread = threading.Thread(target=scan_port, args=(ip, port, port_status))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return port_status


if __name__ == "__main__":
    start_port = int(input("Enter the starting port for scanning (1-65535): "))

    # Store the port number and the status in a .csv extension file to view online or in the IDE.
    with open('port_status.csv', 'w') as f:
        f.write("Port Number,Status\n")
        scanned_ports = scan_ports(start_port, ip="YOUR_IP_HERE")
        for port, status in scanned_ports:
            f.write(f"{port}, {status}\n")

    # Store just the port numbers in a text file.
    with open("ports.txt", "w") as f:
        scanned_ports_str = "\n".join(str(port) for port, status in scanned_ports)
        f.write(scanned_ports_str)
