import requests
from bs4 import BeautifulSoup
import csv

# Oracle's Elixir에서 경기 목록 페이지 (2024 WORLDS 예시)
MATCH_LIST_URL = "https://oracleselixir.com/match-data/teams"

def get_match_ids():
    response = requests.get(MATCH_LIST_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    match_ids = []
    table_rows = soup.select("table tbody tr")

    for row in table_rows:
        link = row.find("a", href=True)
        if link and "/matches/" in link['href']:
            match_id = link['href'].split("/matches/")[-1]
            match_ids.append(match_id)

    return match_ids

def save_to_csv(match_ids, output_file="../data/oracle_match_ids.csv"):
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["match_id"])
        for mid in match_ids:
            writer.writerow([mid])
    print(f"✅ Saved {len(match_ids)} match IDs to {output_file}")

if __name__ == "__main__":
    match_ids = get_match_ids()
    save_to_csv(match_ids)



