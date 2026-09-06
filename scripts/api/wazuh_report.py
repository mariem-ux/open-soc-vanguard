import requests
import urllib3
from datetime import datetime

urllib3.disable_warnings()

# wazuh API credentials
WAZUH_API = "https://localhost:55000"
USER = "wazuh"
PASSWORD = "NewPassword123*"

# get JWT token
def get_token():
    response = requests.post(
        f"{WAZUH_API}/security/user/authenticate",
        auth=(USER, PASSWORD),
        verify=False
    )
    print("Response:", response.json())
    token = response.json()['data']['token']
    print("**Authentification successful ! ")
    return token

##########
def get_alerts(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{WAZUH_API}/manager/logs/summary",
        headers=headers,
        verify=False
    )
    return response.json()

##########
def parse_alerts(data):
    results = []
    items = data['data']['affected_items'][0]
    # step1:loop
    for component, stats in items.items():
        # step2:extract
        if stats['error'] > 0 or stats['warning'] > 0 or stats['critical'] > 0:
            results.append({
                "component": component,
                "errors": stats['error'],
                "warnings": stats['warning'],
                "critical": stats['critical']
            })
    return results

def generate_report(alerts):
    print("\n# Wazuh High-severity Report")
    print(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    print("| Component | Errors | Warning | Critical |")
    print("|-----------|--------|---------|----------|")
    if not alerts:
        print("|No issues found|0       | 0       |0         |")
    else:
        for a in alerts:
            print(f"| {a['component']} | {a['errors']} | {a['warnings']} | {a['critical']} |")

if __name__ == "__main__":
    token = get_token()
    print(f"Token : {token[:50]}...")
    data = get_alerts(token)
    alerts = parse_alerts(data)
    print(f"\nFound {len(alerts)} components with issues\n")
    for a in alerts:
        print(f"-{a['component']} | errors:{a['errors']} warnings:{a['warnings']} critical:{a['critical']}")
    generate_report(alerts)