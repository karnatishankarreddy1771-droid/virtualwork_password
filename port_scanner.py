import socket

def check_port(host, port):

    try:
        # Create a socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout
        s.settimeout(3)

        # Try connecting to the given port
        result = s.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED or FILTERED")

        s.close()

    except socket.gaierror:
        print("Invalid hostname or IP address")

    except ValueError:
        print("Invalid port number")

    except socket.error:
        print("Connection error")


# Main program
host = input("Enter IP address or hostname: ")

try:
    port = int(input("Enter port number: "))

    if 1 <= port <= 65535:
        check_port(host, port)
    else:
        print("Port must be between 1 and 65535")

except ValueError:
    print("Please enter a valid port number")