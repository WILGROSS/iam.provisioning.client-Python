import json
import requests

API_URL = "???" # Skicka in url för att anropa basic eller advanced beroende på vilket betyg du siktar på!
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "???", # Något med APINyckel?
    # VG, saknas det en header här?
}


def load_active_users(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        users = json.load(f)
    return [u for u in users] # VG hur kan man få ut bara aktiva användare?


def build_payload(user):
    # G Här saknas namn och email!
    return {
        "department": user["department"],
        "isActive": user["isActive"],
    }


def provision_users():
    active_users = load_active_users("users.json")
    print(f"Hittade {len(active_users)} aktiva användare att provisionera.\n")

    payloads = [build_payload(user) for user in active_users]

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payloads)
        response.raise_for_status()
        print(f"Success ({response.status_code}): {response.text}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    provision_users()
