"""
Handles logging for both files and databases.
"""

from config import LOG_FILE
from database import insert_log

def log_to_file(data):
    """Logs attacker activity to a file."""
    with open(LOG_FILE, "a") as log_file:
        log_file.write(data + "\n")

def log_activity(ip_address, username=None, password=None, message=None):
    """
    Logs activity to both a file and the database.
    """
    log_entry = f"IP: {ip_address}, Username: {username}, Password: {password}, Message: {message}"
    log_to_file(log_entry)
    insert_log(ip_address, username, password, message)
