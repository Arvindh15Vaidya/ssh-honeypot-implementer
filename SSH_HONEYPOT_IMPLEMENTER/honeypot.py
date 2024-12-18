"""
Core SSH honeypot implementation.
"""

import socket
import threading
import paramiko
from config import HOST, PORT
from logger import log_activity

# Generate a fake SSH server key for encryption
host_key = paramiko.RSAKey.generate(2048)

class SSHServer(paramiko.ServerInterface):
    """Handles SSH server behavior."""

    def __init__(self, ip_address):
        self.event = threading.Event()
        self.client_ip = ip_address

    def check_channel_request(self, kind, chanid):
        """Accepts session channels."""
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        """
        Logs login attempts to the database and file.
        """
        log_activity(self.client_ip, username, password, "Login attempt")
        return paramiko.AUTH_FAILED

def start_honeypot():
    """
    Starts the SSH honeypot to capture malicious activities.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(100)

    print(f"Honeypot running on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        ip_address = client_address[0]
        print(f"Connection from {ip_address}")

        try:
            transport = paramiko.Transport(client_socket)
            transport.add_server_key(host_key)
            server = SSHServer(ip_address)
            transport.start_server(server=server)

            channel = transport.accept(20)
            if channel is None:
                continue
            channel.close()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()
