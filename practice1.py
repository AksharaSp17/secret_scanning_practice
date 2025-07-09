# app.py

"""
This is a mock application for testing secret detection tools like TruffleHog.
All secrets below are FAKE and used for learning/testing purposes only.
"""

import requests
import psycopg2

# === Configuration ===

CONFIG = {
    "aws_access_key": "AKIAIOSFODNN7EXAMPLE",
    "aws_secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "slack_token": "xoxb-123456789012-ABCDEFGHIJKLMNO",
    "google_api_key": "AIzaSyA-abc1234567890defGHIJKLMNOPQ",
    "generic_api_key": "12345-ABCDE-67890-FGHIJ-12345",
    "db_connection_string": "postgres://user:password@localhost:5432/dbname",
    "username": "admin",
    "password": "SuperSecretPassword123",
    "rsa_private_key": """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAsdfsf3242sdf34234sdfsdf
asdf1234asdf1234asdf1234asdf1234asdf1234
asdf1234asdf1234asdf1234asdf1234asdf1234
-----END RSA PRIVATE KEY-----"""
}

# === Simulated AWS Connection ===

def connect_to_aws():
    print("[AWS] Connecting with access key:", CONFIG["aws_access_key"])
    # simulate AWS call
    return True

# === Simulated Slack Notification ===

def notify_slack(message):
    print("[Slack] Sending message with token:", CONFIG["slack_token"])
    # requests.post("https://slack.com/api/chat.postMessage", headers=...)
    return True

# === Simulated Google API Call ===

def call_google_maps():
    print("[Google] Calling Maps API with key:", CONFIG["google_api_key"])
    # requests.get("https://maps.googleapis.com/maps/api/...", params=...)
    return True

# === Simulated DB Connection ===

def connect_to_db():
    print("[DB] Connecting with URL:", CONFIG["db_connection_string"])
    # psycopg2.connect(CONFIG["db_connection_string"])
    return True

# === Main App Logic ===

def run():
    print("== Starting Mock App with Fake Secrets ==")
    connect_to_aws()
    notify_slack("Fake message to #general")
    call_google_maps()
    connect_to_db()
    print("Logged in with user:", CONFIG["username"], "and password:", CONFIG["password"])
    print("RSA Key (preview):", CONFIG["rsa_private_key"][:60], "...")

if __name__ == "__main__":
    run()
