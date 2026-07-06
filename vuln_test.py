import requests

API_KEY = "AKIAIOSFODNN7EXAMPLE"  # intentionally hardcoded for scan test

def call_service():
    return requests.get("https://api.example.com", headers={"Authorization": API_KEY})
