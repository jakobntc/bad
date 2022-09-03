from pprint import pprint

from models import Character

import requests
import pydantic

BASE_URL = "https://raider.io/api/v1/characters/profile?"
REGION = "us"

def get_data(url: str):
    print()


def get_character(realm: str, name: str) -> Character:
    r = requests.get(f"{BASE_URL}region={REGION}&realm={realm}&name={name}")
    if r.status_code == 200:
        pprint(r.json())
        # char = Character.parse_raw(r.text)
        # return char
    else:
        print(f"Hello person, there's a {r.status_code} error with your request")



if __name__ == "__main__":
    # get_data(url=BASE_URL)
    get_character("tichondrius", "saddledk")