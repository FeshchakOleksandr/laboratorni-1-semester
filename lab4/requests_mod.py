import requests

def run_requests():
    r = requests.get("https://api.github.com")
    print(f"Статус відповіді від GitHub: {r.status_code}")