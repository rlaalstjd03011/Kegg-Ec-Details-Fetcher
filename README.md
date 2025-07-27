# KEGG EC Details Fetcher

This project fetches detailed information from KEGG for a list of EC (Enzyme Commission) numbers.  
The data is retrieved using the KEGG REST API and saved as text files for each EC number.

## 🔍 Features

- Reads EC numbers from a `.txt` file (one per line)
- Fetches information from the KEGG database
- Saves each EC number's data as a separate `.txt` file
- Automatically handles filenames safely for all platforms

## Flow Diagram

```
START
  │
  │
  ├── 🔹[1] Load EC number list
  │       - File name: 'ath_all_ec_number.txt'
  │       - Read line by line and add 'ec:' prefix
  │       - Example: 1.1.1.1 → ec:1.1.1.1
  │
  └──▶ Store into ec_ids list
              │
              ▼
  ┌─────────────────────────────────────────────┐
  │ 🔁 [2] For each EC number in ec_ids list     │
  └─────────────────────────────────────────────┘
              │
              ▼
  ┌─────────────────────────────────────────────────┐
  │   Function: fetch_details_from_kegg(ec_id, dir) │
  └─────────────────────────────────────────────────┘
              │
              ▼
  [Send request to KEGG]
    🔸 url = f'https://rest.kegg.jp/get/{ec_id}'
    🔸 response = requests.get(url)

              │
              ▼
  [Check response status]
    🔸 if response.status_code == 200:
          │
          │
          ▼
      [Generate safe file path]
        🔸 safe_filename = ec_id.replace(...)
        🔸 file_path = os.path.join(output_dir, safe_filename.txt)

          │
          ▼
      [Save text to file]
        🔸 with open(file_path, 'w', encoding='utf-8') as file:
               file.write(response.text)

              │
              ▼
  ◀────── Repeat until all EC numbers are processed
              │
              ▼
       ✅ All EC numbers have been processed
              │
              ▼
       --- KEGG Fetching Task Complete ---
```


       
