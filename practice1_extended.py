# extended_app.py

"""
🚨 WARNING: This file contains FAKE secrets for testing secret scanners.
DO NOT use real credentials. Intended for safe, educational, and offline use only.
"""

import os
import requests
import psycopg2

# === Configuration with Fake Secrets ===

CONFIG = {
    "aws_access_key": "AKIAIOSFODNN7EXAMPLE",
    "aws_secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "google_api_key": "AIzaSyA-abc1234567890defGHIJKLMNOPQ",
    "slack_token": "xoxb-123456789012-ABCDEFGHIJKLMNO",
    "github_token": "ghp_AbC123def456GHI789jklMNOpqrSTUvwxYZ",
    "stripe_secret": "sk_test_4eC39HqLyjWDarjtT1zdp7dc",
    "twilio_sid": "AC12345678901234567890123456789012",
    "twilio_auth_token": "your_auth_token_1234567890abcdef",
    "sendgrid_api_key": "SG.xxxxxxxx.yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
    "generic_api_key": "12345-ABCDE-67890-FGHIJ-12345",
    "db_connection_string": "postgres://user:password@localhost:5432/testdb",
    "username": "testuser",
    "password": "TestPass!1234",
    "jwt_secret": "supersecretjwtkey1234567890",
    "rsa_private_key": """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAsdfsf3242sdf34234sdfsdf
asdf1234asdf1234asdf1234asdf1234asdf1234
asdf1234asdf1234asdf1234asdf1234asdf1234
-----END RSA PRIVATE KEY-----"""
}

# === Simulated Service Functions ===

def connect_to_aws():
    print(f"[AWS] Using Access Key: {CONFIG['aws_access_key']}")

def call_google_maps():
    print(f"[Google Maps] API Key: {CONFIG['google_api_key']}")

def send_slack_notification():
    print(f"[Slack] Token: {CONFIG['slack_token']}")

def connect_to_database():
    print(f"[PostgreSQL] Connecting with: {CONFIG['db_connection_string']}")

def access_github():
    print(f"[GitHub] Token: {CONFIG['github_token']}")

def charge_via_stripe():
    print(f"[Stripe] Secret Key: {CONFIG['stripe_secret']}")

def send_sms_twilio():
    print(f"[Twilio] SID: {CONFIG['twilio_sid']}, Token: {CONFIG['twilio_auth_token']}")

def send_email_sendgrid():
    print(f"[SendGrid] API Key: {CONFIG['sendgrid_api_key']}")

def generate_jwt():
    print(f"[JWT] Secret: {CONFIG['jwt_secret']}")

def login_user():
    print(f"[Auth] Username: {CONFIG['username']}, Password: {CONFIG['password']}")

def print_rsa_preview():
    print("[RSA] Private Key (truncated):")
    print(CONFIG['rsa_private_key'][:60] + "...")

# === Main Execution ===

def run():
    print("🚀 Running Extended Mock App with Fake Secrets\n")
    connect_to_aws()
    call_google_maps()
    send_slack_notification()
    access_github()
    charge_via_stripe()
    send_sms_twilio()
    send_email_sendgrid()
    connect_to_database()
    generate_jwt()
    login_user()
    print_rsa_preview()
    print("\n✅ Done. All secrets above are fake and safe for testing.")

if __name__ == "__main__":
    run()
