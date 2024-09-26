import os
import requests
import sys

def add_txt_record(domain, txt_value, api_token, zone_id):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    data = {
        "type": "TXT",
        "name": f"_acme-challenge.{domain}",
        "content": txt_value,
        "ttl": 120
    }
    response = requests.post(url, json=data, headers=headers)
    return response.status_code == 200

if __name__ == "__main__":
    domain = sys.argv[1]
    txt_value = sys.argv[2]
    api_token = sys.argv[3]
    zone_id = sys.argv[4]
    if add_txt_record(domain, txt_value, api_token, zone_id):
        print("Successfully added TXT record.")
    else:
        print("Failed to add TXT record.")
