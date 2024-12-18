'''import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.naturalstattrick.com/playerteams.php?fromseason=20242025&thruseason=20242025&stype=2&sit=5v5&score=all&stdoi=oi&rate=n&team=ALL&pos=S&loc=B&toi=0&gpfilt=none&fd=&td=&tgp=410&lines=single&draftteam=ALL"

req = requests.get(url)
print(req.status_code)

soup = BeautifulSoup(req.content, "html.parser")
rows = soup.find_all("tr")

player_data = []

for row in rows:
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]
    if cols:
        player_data.append(cols)

header_row = soup.find("thead")
if header_row:
    headers = [th.text.strip() for th in header_row.find_all("th")]
else:
    headers = None

if headers:
    df = pd.DataFrame(player_data, columns=headers)
else:
    df = pd.DataFrame(player_data)

print(df.head())
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.naturalstattrick.com/playerteams.php?fromseason=20242025&thruseason=20242025&stype=2&sit=5v5&score=all&stdoi=oi&rate=n&team=ALL&pos=S&loc=B&toi=0&gpfilt=none&fd=&td=&tgp=410&lines=single&draftteam=ALL"

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

rows = soup.find_all("tr")

player_data = []
for row in rows:
    cols = row.find_all("td")  
    cols = [col.text.strip() for col in cols]  
    if len(cols) > 1: 
        player_data.append(cols)
    else:
        print("There is an empty row")

print(player_data)

header_row = soup.find("thead")
if header_row:
    headers = [th.text.strip() for th in header_row.find_all("th")]
else:
    headers = None

if headers:
    df = pd.DataFrame(player_data, columns=headers)
else:
    df = pd.DataFrame(player_data)

print(f"Number of players scraped: {len(df)}")

print(df)

