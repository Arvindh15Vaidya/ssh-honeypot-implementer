"""
Configuration file to store constants like host, port, and database credentials.
"""

# Server configuration
HOST = "192.168.137.216"  # Change to your server's IP
PORT = 2222

# MySQL Database configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1504",
    "database": "honeypot_logs"
}

# Log file path
LOG_FILE = "honeypot.log"
