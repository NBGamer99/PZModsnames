import requests
import re
from bs4 import BeautifulSoup
import argparse


def extract_ids(workshop_id):

    url = f"https://steamcommunity.com/sharedfiles/filedetails/?id={workshop_id}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    description_div = soup.find('div', {'class': 'workshopItemDescription'})
    description_text = description_div.get_text()

    workshop_id_value = re.search('Workshop ID: (\d+)', description_text).group(1)
    mod_id_value = re.search('Mod ID: (\w+)', description_text).group(1)

    return workshop_id_value, mod_id_value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract Workshop IDs and Mod IDs from Steam Community.")
    parser.add_argument('workshop_ids', type=str, help='a semicolon-separated list of Workshop IDs\t e.g. 123456;654321')
    args = parser.parse_args()

    workshop_ids_list = args.workshop_ids.split(';')

    workshop_ids_extracted = []
    mod_ids_extracted = []

    for workshop_id in workshop_ids_list:
        workshop_id_value, mod_id_value = extract_ids(workshop_id)
        workshop_ids_extracted.append(workshop_id_value)
        mod_ids_extracted.append(mod_id_value)

    print(f"Workshop IDs: {', '.join(workshop_ids_extracted)}")
    print(f"Mod IDs: {', '.join(mod_ids_extracted)}")

