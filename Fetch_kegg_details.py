# KEGG REST API에서 EC 번호별 상세 정보를 가져와서 파일로 저장하는 자동화 스크립트

import re
from typing import Set
import os
import requests
import pandas as pd

# Bring details of ec numbers from kegg

def fetch_details_from_kegg(id: str, output_dir: str):
    url = f'https://rest.kegg.jp/get/{id}'

    response = requests.get(url)

    if response.status_code == 200:

        safe_filename = id.replace(":", "_").replace("/", "_").replace("\\", "_")

        file_path = os.path.join(output_directory, f"{safe_filename}.txt") # kegg_details라는 폴더에 파일들을 저장.

        with open(file_path, "w", encoding="utf-8") as file:

            file.write(response.text)

    else:

        print(f"Failed to fetch data for {id}. Status Code: {response.status_code}")

if __name__ == '__main__':
    ec_numbers_input_file = 'ath_all_ec_number.txt'

    output_directory = 'kegg_details'
    os.makedirs(output_directory, exist_ok=True) # 폴더 생성

    ec_ids = []
    try:
        with open(ec_numbers_input_file, "r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    if not stripped_line.startswith("ec"):
                        ec_ids.append(f'ec:{stripped_line}')
                    else:
                        ec_ids.append(stripped_line)

    except FileNotFoundError:
        print(f'File {ec_numbers_input_file} not found.')
        exit()

    for ec_id in ec_ids:
        fetch_details_from_kegg(ec_id, output_directory)

    print('\n--- EC Number fetching Task Complete ---')