import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = 'https://www.skysports.com/premier-league-table/2011'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

league = soup.find_all('table', class_ = 'standing-table__table')
league_table = soup.find_all('tbody')

for league_teams in league_table:
    rows = league_teams.find_all('tr')
    for row in rows:
        player_teams = row.find('td', class_ = 'standing-table__cell standing-table__cell--name').text.strip()
        player_points = row.find_all('td', class_ = 'standing-table__cell')[9].text
       
df = pd.DataFrame[['player_points'], ['player_teams']]
print(df)


