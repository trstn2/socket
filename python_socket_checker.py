import socket

def port_selection():
    local_ip = "YOUR_LOCAL_IP_HERE"
    ip = "YOUR_IP_HERE"
    s_selection = int(input("Enter the port you would like to check for: "))
    try:
        if 1 <= s_selection <= 65535:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, s_selection))
                print(f"Port {s_selection} is open on ip {ip}.")
    except ConnectionRefusedError:
        print(
            f"Could not connect to the server at {ip}:{s_selection}. Please check the server status and network settings.")

    try:
        if 1 <= s_selection <= 65535:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((local_ip, s_selection))
                print(f"Port {s_selection} is open on local ip: {local_ip}.")
    except ConnectionRefusedError:
        print(
            f"Could not connect to the server at {local_ip}:{s_selection}. Please check the server status and network settings.")


if __name__ == "__main__":
    port_selection()